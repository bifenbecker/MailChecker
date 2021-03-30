import base64
import email
import os
import sqlite3,ExceptionBreak,imaplib,asyncio

class MailData():

    # def __init__(self,mails):
    #     try:
    #         self.add_to_data_base(mails)
    #     except:
    #         raise ExceptionBreak("Failed to load records")

    @staticmethod
    def add_to_data_base(line,DB_NAME="MAILS.db"):
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS mails(mail TEXT, password TEXT, valid INT)""")
        connection.commit()

        if ":" in line and "@" in line.split(":")[0]:
            mail = [line.split(":")[0], line.split(":")[-1]]
            sql = "SELECT mail FROM mails WHERE mail = ?"
            cursor.execute(sql, (mail[0],))
            DB = cursor.fetchall()
            if not DB:
                imap_conn = int(MailData.check_imap_connection(mail))
                mail.append(imap_conn)
                cursor.execute("INSERT INTO mails VALUES (?,?,?)", mail)
        else:
            cursor.execute("INSERT INTO mails VALUES (?,?,?)", (line,"", 0))


        connection.commit()


    @staticmethod
    def get_mails(user,name):
        user_ = user.split(":")
        DB_NAME = os.path.join('sessions', name, f'{name}.db')
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS mails(email TEXT, password TEXT, seen INT, date TEXT, subject TEXT, from_ TEXT, type TEXT, content TEXT)""")
        connection.commit()
        conn = imaplib.IMAP4_SSL('imap.gmail.com')#
        imap_user = user_[0]
        imap_password = user_[1]

        conn.login(imap_user,imap_password)
        conn.select()
        res,data = conn.uid('search',None,'(UNSEEN)')
        assert res == 'OK'
        inbox_item_list = data[0].split()
        for item in inbox_item_list:
            try:
                result, data = conn.uid('fetch', item, '(RFC822)')
            except:
                continue
            assert result == 'OK'
            raw_email = data[0][1].decode("latin-1")
            parts = MailData.get_parts_mail(raw_email,0)
            cursor.execute("INSERT INTO mails VALUES (?,?,?,?,?,?,?,?)", user_ + parts)
            connection.commit()

        res, data = conn.uid('search', None, '(SEEN)')
        assert res == 'OK'
        inbox_item_list = data[0].split()[-3:]
        for item in inbox_item_list:
            try:
                result, data = conn.uid('fetch', item, '(RFC822)')
            except:
                continue
            assert result == 'OK'
            raw_email = data[0][1].decode("latin-1")
            parts = MailData.get_parts_mail(raw_email,1)
            cursor.execute("INSERT INTO mails VALUES (?,?,?,?,?,?,?,?)", user_ + parts)
            connection.commit()

    @staticmethod
    def get_parts_mail(mail,SEEN):
        email_message = email.message_from_string(mail)
        seen = SEEN
        date = email_message['date']
        from_ = MailData._clear_subject(email_message['From'])
        subject_ = MailData._clear_subject(email_message['Subject'])
        for part in email_message.walk():
            if part.get_content_maintype() == 'multipart':
                continue
        type = part.get_content_type().split('/')[1]
        content = part.get_payload(decode=True)
        return [seen,date,subject_,from_,type,content]

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

    @staticmethod
    def load_imap(mail,path):
        DB_NAME = os.path.join('sessions',path,f'{path}.db')
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS mails(mail TEXT, password TEXT, valid INT)""")
        connection.commit()

        if ":" in mail and "@" in mail.split(":")[0]:
            user_mail = mail.split(":")[0]
            user_passwd = mail.split(":")[-1]
            sql = "SELECT mail FROM mails WHERE mail = ?"
            cursor.execute(sql, (user_mail,))
            DB = cursor.fetchall()
            connection.commit()
            if not DB:
                conn = MailData.check_imap_connection((user_mail,user_passwd))
                db_data = (user_mail,user_passwd,int(conn))
                cursor.execute("INSERT INTO mails VALUES (?,?,?)",db_data)
                connection.commit()
        else:
            cursor.execute("INSERT INTO mails VALUES (?,?,?)", (mail,"", 0))
            connection.commit()


    @staticmethod
    def check_imap_connection(mail):
        imap_user = mail[0]
        imap_password = mail[1]
        SERVER = "imap.{}".format(imap_user.split("@")[-1])
        try:
            conn = imaplib.IMAP4_SSL(SERVER)
            res, data = conn.login(imap_user, imap_password)
        except:
            #Check default google server
            try:
                conn = imaplib.IMAP4_SSL("imap.gmail.com")
                res, data = conn.login(imap_user, imap_password)
            except:
                res = 'No'
        return True if res == 'OK' else False


    async def IMAP_connection(self):
        success = 0
        connection = sqlite3.connect(self.DB_NAME)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM mails")
        mails = cursor.fetchall()

        for mail in mails:
            self.check_imap_connection(mail)
            await asyncio.sleep(0.01)

        print(success,len(mails)-success)

