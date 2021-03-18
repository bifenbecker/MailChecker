import sqlite3,ExceptionBreak,imaplib,asyncio

class MailData():

    DB_NAME = "MAILS.db"

    def __init__(self,mails):
        try:
            self.add_to_data_base(mails)
            self.IMAP_connection()
        except:
            raise ExceptionBreak("DB error")

    def add_to_data_base(self,mails):
        connection = sqlite3.connect(self.DB_NAME)
        cursor = connection.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS mails(mail TEXT, password TEXT)""")
        connection.commit()


        for mail in mails:
            sql = "SELECT mail FROM mails WHERE mail = ?"
            cursor.execute(sql, (mail[0],))
            DB = cursor.fetchall()
            if DB:
                continue
            else:
                cursor.execute("INSERT INTO mails VALUES (?,?)", mail)
        connection.commit()

    async def check_imap_connection(self,mail):
        imap_user = mail[0]
        imap_password = mail[1]
        conn = imaplib.IMAP4_SSL("imap.{}".format(imap_user.split("@")[-1]))
        try:
            res, data = conn.login(imap_user, imap_password)
        except:
            res = "No"
        return True if res == 'OK' else False


    async def IMAP_connection(self):
        success = 0
        connection = sqlite3.connect(self.DB_NAME)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM mails")
        mails = cursor.fetchall()
        for mail in mails:
            await check_imap_connection(mail)

        print(success,len(mails)-success)

