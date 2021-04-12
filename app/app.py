import time

import emaillib
from emaillib import IMAP

from database import SQLiteDB
from database import Account, Message

import os
from datetime import datetime

from pony import orm
import threading

import selectors

selector = selectors.DefaultSelector()


def get_accounts(file_path: str = "data\\mails.txt", separator: str = ':') -> list:
    """Parse text file to retrieve logins and passwords and return it"""

    accounts = []

    with open(file_path, 'r') as file:
        lines = file.read().split('\n')

        for line in lines:
            data_list = line.split(separator)
            accounts.append({"login": data_list[0], "password": data_list[1]})

    return accounts


def get_messages(conn: IMAP, uids_list: list) -> list:
    """Get messages from email address and fill messages field of IMAP instance

    uids_list - list of messages id's to receive messages"""

    messages = []

    for uid in uids_list:

        print('message uid: ', uid)

        message = conn.get_message(uid)

        if message:
            messages.append(message)

    return messages


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

    elif not os.path.exists(save_path):
        os.makedirs(save_path)

        open(os.path.join(save_path, "GOOD.txt"), 'w')
        open(os.path.join(save_path, "BAD.txt"), 'w')
        open(os.path.join(save_path, "ERROR.txt"), 'w')

        rm_dir = False

    save_info = f"{account['login']}:{account['password']}\n"

    try:
        conn = protocol(account['login'], account['password'], secure=True)
        account['is_valid'] = True

        with open(os.path.join(save_path, "GOOD.txt"), 'a') as good:
            good.write(save_info)

    except emaillib.imap.Error:
        account['is_valid'] = False
        conn = None

        with open(os.path.join(save_path, "BAD.txt"), 'a') as bad:
            bad.write(save_info)

    except Exception:
        with open(os.path.join(save_path, "ERROR.txt"), 'a') as error:
            error.write(save_info)

        print("Done")
        return None, None

    unique_fields = {
        'login': account["login"]
    }

    acc = db.add_in_table(Account, data=account, unique_fields=unique_fields)[1]

    print("Done")

    if conn:
        amount = add_messages(db, conn, acc, search_params or {})
        log_query(save_path, search_params["_filter"], account, amount)

    return conn, acc


def log_query(save_path: str, query: str, account: dict, amount: int):
    """Log query in file with stats by accounts"""

    global rm_log

    save_path = os.path.join(save_path, f"{query}.txt")

    if rm_log:
        open(save_path, 'w')
        rm_log = False

    with open(save_path, 'a') as file:
        file.write(f"{account['login']}:{account['password']} | {amount}\n")


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

        # conn, acc = validation(db, IMAP, account, save_path, dir_name)

        thread = threading.Thread(target=validation, args=(db, IMAP, account, save_path, dir_name))
        thread.start()

        # if conn:
        #     # thread = threading.Thread(target=add_messages, args=(db, conn, acc, search_params or {}))
        #     # thread.start()
        #     amount = add_messages(db, conn, acc, search_params or {})
        #     log_query(os.path.join(save_path, dir_name), search_params["_filter"], account, amount)


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
        "_to": 100,
    }

    print(IMAP.get_filter(filters), end='\n\n')

    accounts_list = get_accounts(file_path, separator=':')

    _main(sqlite_db, accounts_list[:], save_path, file_name, search_params)

    # sqlite_db.show_table(Account, end='\n\n')
    # sqlite_db.show_table(Message)
