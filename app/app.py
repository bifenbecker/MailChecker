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
def validation(db: SQLiteDB, protocol: IMAP, account: dict, save_path: str, dir_name: str) -> tuple:
    """Validate account with creating logs, adding in database and returning connection"""

    global rm_dir

    save_path = os.path.join(save_path, dir_name)

    if os.path.exists(save_path) and rm_dir:
        open(os.path.join(save_path, "GOOD.txt"), 'w')
        open(os.path.join(save_path, "BAD.txt"), 'w')
        open(os.path.join(save_path, "ERROR.txt"), 'w')

        rm_dir = False

    if not os.path.exists(save_path):
        os.makedirs(save_path)

        open(os.path.join(save_path, "GOOD.txt"), 'w')
        open(os.path.join(save_path, "BAD.txt"), 'w')
        open(os.path.join(save_path, "ERROR.txt"), 'w')

    save_info = f"{account['login']}:{account['password']}\n"

    try:
        conn = protocol(account['login'], account['password'], secure=True)
        account['is_valid'] = True

        with open(os.path.join(save_path, "GOOD.txt"), 'a') as good:
            good.write(save_info)

    except emaillib.imap.Error:
        account['is_valid'] = False

        with open(os.path.join(save_path, "BAD.txt"), 'a') as bad:
            bad.write(save_info)

        return None, None

    except Exception:
        with open(os.path.join(save_path, "ERROR.txt"), 'a') as error:
            error.write(save_info)

        return None, None

    unique_fields = {
        'login': account["login"]
    }

    acc = db.add_in_table(Account, data=account, unique_fields=unique_fields)[1]

    return conn, acc


def log_query(save_path: str, query: str, account: dict, amount: int):
    """Log query in file with stats by accounts"""

    global rm_log

    save_path = os.path.join(save_path, query)

    if os.path.exists(save_path) and rm_log:
        open(save_path, 'w')
        rm_log = False
    elif not os.path.exists(save_path):
        open(save_path, 'w')

    with open(save_path, 'a') as file:
        file.write(f"{account['login']}:{account['password']} | {amount}\n")


@orm.db_session
def add_messages(db: SQLiteDB, conn: IMAP, acc: Account, search_params: dict) -> int:
    """Add messages to Message table in database"""

    uids_list = conn.get_uids(**search_params)

    for message in conn.get_messages(uids_list):
        message["owner"] = acc

        unique_fields = {
            'sender': message["sender"],
            'content': message["content"],
        }

        db.add_in_table(Message, data=message, unique_fields=unique_fields)

    return len(uids_list)


@orm.db_session
def _main(db: SQLiteDB, accounts_list: list, save_path: str, dir_name: str, search_params: dict = None):
    """Check accounts, retrieve all messages and add it to database"""

    for account in accounts_list:

        print('\naccount:', accounts_list.index(account), account["login"])

        conn, acc = validation(db, IMAP, account, save_path, dir_name)

        # thread = threading.Thread(target=add_messages, args=(imap, db, acc))
        # thread.start()

        if not search_params:
            search_params = {}

        if conn and acc:
            amount = add_messages(db, conn, acc, search_params)
            log_query(os.path.join(save_path, dir_name), search_params["_filter"], account, amount)


if __name__ == '__main__':

    db_location = os.path.join(os.getcwd(), 'database.sqlite')
    create_db = True
    create_tables = True

    sqlite_db = SQLiteDB(db_location, create_db, create_tables)

    rm_dir = True
    rm_log = True
    file_path = "data\\mails.txt"
    file_name = file_path.split('\\')[-1]
    save_path = ""

    filters = {
        "new": False,
        "in_header": False,
        "in_body": False,
        "since": False,
        "before": False,
        "on": False,
        "string": "Hi",
    }
    search_params = {
        "folder": "INBOX",
        "_filter": IMAP.get_filter(filters),
        "_from": 0,
        "_to": 10,
    }

    print(IMAP.get_filter(filters), end='\n\n')

    accounts_list = get_accounts("data\\mails.txt", separator=':')
    _main(sqlite_db, accounts_list[:10], save_path, file_name, search_params)

    # sqlite_db.show_table(Account, end='\n\n')
    # sqlite_db.show_table(Message)
