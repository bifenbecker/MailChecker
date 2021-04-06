import poplib
import imaplib

# mail = poplib.POP3_SSL('pop.poortenaar.com')
# mail.user('info@poortenaar.com')
# mail.pass_('78jeroen')
# print(mail.list())

# mail = imaplib.IMAP4_SSL('imap.poortenaar.com')
# mail.login('info@poortenaar.com', '78jeroen')
# print(mail.list()[0])

# # Выводит список папок в почтовом ящике.
# mail.select("inbox")  # Подключаемся к папке "входящие".
# result, data = mail.search(None, "ALL")
# print(data)
#
# ids = data[0]  # Получаем сроку номеров писем
# id_list = ids.split()  # Разделяем ID писем
# latest_email_id = id_list[-1]  # Берем последний ID
#
# result, data = mail.fetch(latest_email_id, "(RFC822)")  # Получаем тело письма (RFC822) для данного ID
#
# raw_email = data[0][1]  # Тело письма в необработанном виде
# print(raw_email)
# # включает в себя заголовки и альтернативные полезные нагрузки

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
    def clear_subject(subject: str, bad_strings: tuple = (), bad_symbols: str = '/:*?"<>|') -> str:
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
            message["Subject"] = self.clear_subject(msg["Subject"])
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
# accounts = []
# with open("mail.txt") as file:
#     raw_accounts = file.read().split('\n')
#
#     for account in raw_accounts:
#         data_list = account.split(':')
#         accounts.append({"user": data_list[0], "password": data_list[1]})
#
# for account in accounts:
#     print(account)
#
# imap = IMAP("ikomicin@gmail.com", "password", secure=True)
# db = SQLiteDB("email_db")
#
# for message in imap.get_messages(_to=5):
#     fields_list = (message["Folder"],
#                    message["Subject"],
#                    message["Content-Extension"],
#                    message["Content"],)
#
#     db.update_table(fields_list, table_name="messages")
#
# for message in db.get_table("messages"):
#     print(message)

# path = os.path.join(os.getcwd(), "sessions", name_session)
#             if not os.path.exists(path):
#                 os.makedirs(path)
#                 DB_NAME = os.path.join(path, f'{name_session}.db')
#                 connection = sqlite3.connect(DB_NAME)

# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3

# Создаем соединение с нашей базой данных
# В нашем примере у нас это просто файл базы
conn = sqlite3.connect('Chinook_Sqlite.sqlite')

# Создаем курсор - это специальный объект который делает запросы и получает их результаты
cursor = conn.cursor()

# Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")

# Получаем результат сделанного запроса
results = cursor.fetchall()
results2 = cursor.fetchall()

print(results)   # [('A Cor Do Som',), ('Aaron Copland & London Symphony Orchestra',), ('Aaron Goldberg',)]
print(results2)  # []

# Делаем INSERT запрос к базе данных, используя обычный SQL-синтаксис
cursor.execute("insert into Artist values (Null, 'A Aagrh!') ")

# Если мы не просто читаем, но и вносим изменения в базу данных - необходимо сохранить транзакцию
conn.commit()

# Проверяем результат
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
results = cursor.fetchall()
print(results)  # [('A Aagrh!',), ('A Cor Do Som',), ('Aaron Copland & London Symphony Orchestra',)]

cursor.execute("""
  SELECT name
  FROM Artist
  ORDER BY Name LIMIT 3
""")

# C подставновкой по порядку на места знаков вопросов:
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT ?", ('2'))

# И с использованием именнованных замен:
cursor.execute("SELECT Name from Artist ORDER BY Name LIMIT :limit", {"limit": 3})

# Обратите внимание, даже передавая одно значение - его нужно передавать кортежем!
# Именно по этому тут используется запятая в скобках!
new_artists = [
    ('A Aagrh!',),
    ('A Aagrh!-2',),
    ('A Aagrh!-3',),
]
cursor.executemany("insert into Artist values (Null, ?);", new_artists)

cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
print(cursor.fetchone())    # ('A Cor Do Som',)
print(cursor.fetchone())    # ('Aaron Copland & London Symphony Orchestra',)
print(cursor.fetchone())    # ('Aaron Goldberg',)
print(cursor.fetchone())    # None

# Использование курсора как итератора
for row in cursor.execute('SELECT Name from Artist ORDER BY Name LIMIT 3'):
        print(row)
# ('A Cor Do Som',)
# ('Aaron Copland & London Symphony Orchestra',)
# ('Aaron Goldberg',)

# Не забываем закрыть соединение с базой данных
conn.close()

# Импортируем библиотеку, соответствующую типу нашей базы данных
# В данном случае импортируем все ее содержимое, чтобы при обращении не писать каждый раз имя библиотеки, как мы делали в первой статье
# import peewee as pw

# Создаем соединение с нашей базой данных
# В нашем примере у нас это просто файл базы
# conn = pw.SqliteDatabase('Chinook_Sqlite.sqlite')


# Определяем базовую модель о которой будут наследоваться остальные
# class BaseModel(pw.Model):
#     class Meta:
#         database = conn  # соединение с базой, из шаблона выше


# Определяем модель исполнителя
# class Artist(BaseModel):
#     artist_id = pw.AutoField(column_name='ArtistId')
#     name = pw.TextField(column_name='Name', null=True)
#
#     class Meta:
#         table_name = 'Artist'
#
#
# conn = pw.SqliteDatabase('Chinook_Sqlite.sqlite')

# Создаем курсор - специальный объект для запросов и получения данных с базы
cursor = conn.cursor()

# ТУТ БУДЕТ НАШ КОД РАБОТЫ С БАЗОЙ ДАННЫХ

# Не забываем закрыть соединение с базой данных
conn.close()

# with orm.db_session:
#     for account in accounts_list[:5]:
#
#         try:
#             imap = IMAP(account['login'], account['password'], secure=True)
#             account['is_valid'] = True
#         except emaillib.imap.Error:
#             account['is_valid'] = False
#
#         unique_fields = {
#             'login': account["login"]
#         }
#
#         acc = sqlite_db.add_in_table(Account, data=account, unique_fields=unique_fields)[1]
#
#         if not account['is_valid']:
#             continue
#
#         print(f"login: {account['login']}")
#         print(f"password: {account['password']}")
#         print()
#
#         for message in imap.get_messages(_to=5):
#
#             print(message)
#             message["owner"] = acc
#
#             unique_fields = {
#                 'sender': message["sender"],
#                 'content': message["content"],
#             }
#
#             msg = sqlite_db.add_in_table(Message, data=message, unique_fields=unique_fields)
#
#         print()


def _clear_subject(subject: str, bad_strings: tuple = (), bad_symbols: str = '/:*?"<>|') -> str:
    """Clear subject field in imap response

    subject - string, that will be cleared
    bad_strings - tuple of strings, which will be cleared
    bad_symbols - tuple of symbols, which will be cleared"""

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


def insert_date(s: str, date: str) -> str:
    index = ~s[::-1].index('.')

    return f"{s[:index]}_{date}{s[index:]}"

# str_date = datetime.now().strftime("%d.%m.%Y_%H.%M.%S")
# dir_name = f"{file_name}_{str_date}"

# def get_messages(self, folder: str = "INBOX", _filter: str = "ALL", _from: int = 0, _to: int = 0) -> list:
#     """Get messages from email address and fill messages field of IMAP instance
#
#     folder - folder on imap server, which will be selected (default: "INBOX")
#     _filter - filter to select messages (default: "ALL")
#     _from - lower frame of selection (default: 0)
#     _to - upper frame of selection (default: 0)"""
#
#     self.connection.select(folder)
#
#     result, data = self.connection.uid('search', "", _filter)
#     item_list = data[0].split()
#
#     if not _to:
#         _to = len(item_list)
#
#     for item in item_list[_from:_to]:
#
#         print('message: ', item_list.index(item))
#
#         message = {}
#
#         result, email_data = self.connection.uid('fetch', item, '(RFC822)')
#         raw_email = email_data[0][1].decode("latin-1")
#         msg = email.message_from_string(raw_email)
#
#         # msg = email.message_from_bytes(email_data[0][1])
#
#         result = ""
#         flag = True
#
#         for part in msg.walk():
#
#             content_type = part.get_content_type()
#
#             if 'multipart' in content_type:
#                 continue
#
#             if content_type == 'text/html':
#                 result = part
#                 break
#
#             elif flag and content_type == 'text/plain':
#                 result = part
#                 flag = False
#
#         # print(_structure(msg))
#         # print(result)
#         # print(msg["Delivery-date"])
#         message["date"] = self.get_unix_time(msg["Received"].split('; ')[-1])
#         message["sender"] = msg["From"]
#         message["subject"] = self._clear_subject(msg["Subject"])
#         message["content"] = str(result.get_payload(decode=True))
#         message["content_extension"] = mimetypes.guess_extension(result.get_content_type())
#
#         # message["raw_message"] = msg
#         # message["structure"] = _structure(msg)
#
#         if message not in self.messages:
#             self.messages.append(message)
#
#     return self.messages
