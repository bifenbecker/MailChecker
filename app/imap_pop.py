import base64
import mimetypes
import os
import imaplib
import poplib
import email
from email.iterators import _structure
import sqlite3


class IMAP:
    def __init__(self, address: str, password: str, server: str = "", secure: bool = False):
        self.messages = []

        if not server:
            server = f"imap.{address.split('@')[-1]}"

        if secure:
            self.connection = imaplib.IMAP4_SSL(server)
        else:
            self.connection = imaplib.IMAP4(server)

        self.connection.login(address, password)

    @staticmethod
    def _clear_subject(subject: str, bad_strings: tuple = (), bad_symbols: str = '/:*?"<>|') -> str:
        if not bad_strings:
            bad_strings = ("=?UTF-8?B?", "=?utf-8?B?")

        for s in bad_strings:
            if s in subject:
                subject_list = [base64.b64decode(p).decode('utf-8') for p in subject.split(s)]
                subject = ''.join(subject_list)

                # subject = ''.join(map(lambda x: base64.b64decode(x).decode('utf-8'), msg['Subject'].split(s)))

        for symbol in bad_symbols:
            if symbol in subject:
                subject = subject.replace(symbol, '')

        return subject

    def get_messages(self, folder: str = "INBOX", _filter: str = "ALL", _from: int = 0, _to: int = 0) -> list:
        self.connection.select(folder)

        result, data = self.connection.uid('search', None, _filter)
        item_list = data[0].split()

        if not _to:
            _to = len(data[0].split())

        item_list = item_list[_from:_to]

        for item in item_list:
            message = {}

            result, email_data = self.connection.uid('fetch', item, '(RFC822)')
            raw_email = email_data[0][1].decode("latin-1")
            msg = email.message_from_string(raw_email)

            html = ""
            plain = ""
            for part in msg.walk():

                if part["Content-Type"].startswith('text/html'):
                    html = part
                elif part["Content-Type"].startswith('text/plain'):
                    plain = part

                if part.get_content_maintype() == 'multipart':
                    continue

            result = html if html else plain

            message["Folder"] = folder
            message["Subject"] = self._clear_subject(msg["Subject"])
            # message["Raw-Message"] = msg
            # message["Structure"] = _structure(msg)
            message["Content"] = result.get_payload(decode=True)
            message["Content-Extension"] = mimetypes.guess_extension(result.get_content_type())

            self.messages.append(message)

        return self.messages


class SQLiteDB:
    db_count = 0
    table_count = 0

    def __init__(self, db_name: str = ""):

        if not db_name:
            db_name = f"db_{SQLiteDB.db_count}"

        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        SQLiteDB.db_count += 1

    def exists(self, table: str, field_name: str, field: str) -> bool:
        response = self.cursor.execute(f"""SELECT {field_name} FROM {table} WHERE {field_name}=?""", (field,))

        for row in response:
            print(row[0])

        print(response[0][0])

        return True if response[0][0] else False

    def update_table(self, fields: tuple, table_name: str = ""):

        if not table_name:
            table_name = f"table_{SQLiteDB.table_count}"

        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}
                                (folder text, subject text, content text, content_extension text)""")

        print(fields[-1])
        if not self.exists(table_name, "content", fields[-1]):
            marks = ','.join(['?' for _ in range(len(fields))])
            self.cursor.execute(f"INSERT INTO {table_name} VALUES ({marks})", fields)
            self.connection.commit()

    def get_table(self, table_name: str):
        return self.cursor.execute(f"SELECT * FROM {table_name}")


class POP:
    pass


# imap = imaplib.IMAP4_SSL('imap.gmail.com')
# imap.login('ikomicin@gmail.com', 'NikoNikoNi4')

# All folders
# print(imap.list())

# INBOX folder
# print(imap.select('INBOX'))
# imap.select()

# getting list of messages id
# resp, items = imap.search(None, "ALL")  # you could filter using the IMAP rules here (check http://www.example-code.com/csharp/imap-search-critera.asp)
# items = items[0].split()  # getting the mails id

# for email_id in items:
#
#     # getting mail with id = 1 in data and status code in status
#     status, data = imap.fetch(email_id, '(RFC822)')
#     print(data[0][1])
#
#     # converting data with email lib
#     msg = email.message_from_bytes(data[0][1])
#
#     # Check if any attachments at all
#     if msg.get_content_maintype() != 'multipart':
#         continue
#
#     print("[" + msg["From"] + "] :" + msg["Subject"])
#
#     # we use walk to create a generator so we can iterate on the parts and forget about the recursive headach
#     for part in msg.walk():
#         # multipart are just containers, so we skip them
#         if part.get_content_maintype() == 'multipart':
#             continue

# print(email.utils.parsedate_tz(msg['Date']))

# payload = msg.get_payload()
# for i in payload:
#     print(i, end='\n\n\n')
#
# payload = payload[0]
# print(payload['Content-Type'])
# print(payload.get_payload())
#
# payload = msg.get_payload()
# count = 0
# for m in msg.walk():
#     count += 1
#     print(m.as_string())
#     print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
#
# print(count)


# if __name__ == '__main__':
#     c = imap
#     try:
#         typ, data = c.list(pattern='I*')
#     finally:
#         c.logout()
#     print('Response code:', typ)
#
#     for line in data:
#         print('Server response:', line)


def mail_select(mail):
    result, data = mail.uid('search', None, "ALL")
    inbox_item_list = data[0].split()

    i = 0
    for item in inbox_item_list:
        result, email_data = mail.uid('fetch', item, '(RFC822)')
        # print(email_data)

        raw_email = email_data[0][1].decode("latin-1")
        msg = email.message_from_string(raw_email)
        # print(raw_email)
        # print(msg)
        # print(msg["Date"])
        # print(_structure(msg))

        subject = msg['Subject']
        for s in ("=?UTF-8?B?", "=?utf-8?B?"):

            if s in msg['Subject']:

                subject_list = [base64.b64decode(p).decode('utf-8') for p in msg['Subject'].split(s)]
                subject = ''.join(subject_list)

                # subject = ''.join(map(lambda x: base64.b64decode(x).decode('utf-8'), msg['Subject'].split(s)))

        html = ""
        plain = ""
        for part in msg.walk():

            if part["Content-Type"].startswith('text/html'):
                html = part
            elif part["Content-Type"].startswith('text/plain'):
                plain = part

            if part.get_content_maintype() == 'multipart':
                continue

            filename = part.get_filename()
            if not filename:
                ext = mimetypes.guess_extension(part.get_content_type())
                filename = f'msg-part-00{i}{ext}'

            i += 1

        result = html if html else plain

        for symbol in '/:*?"<>|':
            if symbol in subject:
                subject = subject.replace(symbol, '')

        # save_path = os.path.join(os.getcwd(), 'emails', subject)
        save_path = '1'
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        with open(os.path.join(save_path, filename), 'wb') as file_save:
            file_save.write(result.get_payload(decode=True))

        # print(msg.get_payload(decode=True))
        # print(result.get_payload(decode=True))


# mail_select(imap)
accounts = []
with open("mail.txt") as file:
    raw_accounts = file.read().split('\n')

    for account in raw_accounts:
        data_list = account.split(':')
        accounts.append({"user": data_list[0], "password": data_list[1]})

for account in accounts:
    print(account)

imap = IMAP("ikomicin@gmail.com", "NikoNikoNi4", secure=True)
db = SQLiteDB("email_db")

for message in imap.get_messages(_to=5):
    fields_list = (message["Folder"],
                   message["Subject"],
                   message["Content-Extension"],
                   message["Content"],)

    db.update_table(fields_list, table_name="messages")

for message in db.get_table("messages"):
    print(message)
