from emaillib.imap import IMAP
from emaillib.database import SQLiteDB
import emaillib



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

for account in accounts_list:

    try:
        imap = IMAP(account['login'], account['password'], secure=True)
    except emaillib.imap.Error:
        continue

    db = SQLiteDB("email_db")

    print(f"login: {account['login']}")
    print(f"password: {account['password']}")
    print()

    for message in imap.get_messages(_to=5):

        print(message)

        fields_list = (message["Date"],
                       message["Subject"],
                       message["Content-Extension"],
                       message["Content"],)

        db.update_table(fields_list, table_name="messages")

    for message in db.get_table("messages"):
        print(message)

    print()
