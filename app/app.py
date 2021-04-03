import emaillib
from emaillib.imap import IMAP

from database.models import Account, Message
from database.database import SQLiteDB

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
def add_messages(imap: IMAP, db: SQLiteDB, acc: Account) -> None:
    for message in imap.get_messages(_to=10):
        message["owner"] = acc

        unique_fields = {
            'sender': message["sender"],
            'content': message["content"],
        }

        msg = db.add_in_table(Message, data=message, unique_fields=unique_fields)


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

        thread = threading.Thread(target=add_messages, args=(imap, db, acc))
        thread.start()

        # add_messages(imap, db, acc)


if __name__ == '__main__':
    sqlite_db = SQLiteDB()

    accounts_list = get_accounts("data\\mails.txt", separator=':')
    fill_tables(sqlite_db, accounts_list[:1])

    sqlite_db.show_table(Account, end='\n\n')
    sqlite_db.show_table(Message)
