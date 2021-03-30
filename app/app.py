import emaillib
from emaillib.imap import IMAP

from pony import orm
from database import SQLiteDB
from models import Account, Message


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

with orm.db_session:

    for account in accounts_list[:5]:

        is_valid = True

        try:
            imap = IMAP(account['login'], account['password'], secure=True)
        except emaillib.imap.Error:
            is_valid = False

        acc = Account(login=account["login"],
                      password=account["password"],
                      valid=is_valid)

        # TODO: create function to check acc existence

        if not is_valid:
            continue

        # db = SQLiteDB("email_db")

        # print(f"login: {account['login']}")
        # print(f"password: {account['password']}")
        # print()

        for message in imap.get_messages(_to=5):

            # print(message)

            # fields_list = (message["Date"],
            #                message["Subject"],
            #                message["Content-Extension"],
            #                message["Content"],)
            #
            # db.update_table(fields_list, table_name="messages")

            msg = Message(date=message["Date"],
                          sender=message["From"],
                          subject=message["Subject"],
                          content=message["Content"],
                          content_extension=message["Content-Extension"],
                          owner=acc)

            # TODO: create function to check existence of msg
            # if msg in orm.select(m for m in Message)[:]:
            #     msg.delete()
            #     continue

        # print()

        # for message in db.get_table("messages"):
        #     print(message)

    # TODO: create function to print db
    for a in orm.select(a for a in Account)[:]:
        print(a.login)

        for m in orm.select(m for m in Message if m.owner == a)[:]:
            print('\t-', m.subject)

    # print()
