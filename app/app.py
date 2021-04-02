import emaillib
from emaillib.imap import IMAP

from pony import orm
from database.models import Account, Message
from database.database import SQLiteDB


def get_accounts(file_path: str = "data\\mails.txt", separator: str = ':') -> list:
    """Parse text file to retrieve logins and passwords and return it"""

    accounts = []

    with open(file_path, 'r') as file:
        lines = file.read().split('\n')

        for line in lines:
            data_list = line.split(separator)
            accounts.append({"login": data_list[0], "password": data_list[1]})

    return accounts


accounts_list = get_accounts("data\\mails.txt", separator=':')
sqlite_db = SQLiteDB()

with orm.db_session:
    for account in accounts_list[:5]:

        try:
            imap = IMAP(account['login'], account['password'], secure=True)
            account['is_valid'] = True
        except emaillib.imap.Error:
            account['is_valid'] = False

        unique_fields = {
            'login': account["login"]
        }

        acc = sqlite_db.add_in_table(Account, data=account, unique_fields=unique_fields)[1]

        if not account['is_valid']:
            continue

        print(f"login: {account['login']}")
        print(f"password: {account['password']}")
        print()

        for message in imap.get_messages(_to=5):

            print(message)
            message["owner"] = acc

            unique_fields = {
                'sender': message["sender"],
                'content': message["content"],
            }

            msg = sqlite_db.add_in_table(Message, data=message, unique_fields=unique_fields)

        print()

sqlite_db.show_table(Account)
sqlite_db.show_table(Message)
