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
    async def load_imap(mail):
        DB_NAME = "adb.db"
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS mails(mail TEXT, password TEXT, valid INT)""")
        connection.commit()

        if ":" in mail and "@" in mail.split(":")[0]:
            user_mail = mail.split(":")[0]
            user_passwd = mail.split(":")[-1]
            sql = "SELECT mail FROM mails WHERE mail = ?"
            cursor.execute(sql, (mail[0],))
            DB = cursor.fetchall()
            if not DB:
                conn = await MailData.check_imap_connection((user_mail,user_passwd))
                db_data = (user_mail,user_passwd,int(conn))
                print(db_data)
                cursor.execute("INSERT INTO mails VALUES (?,?,?)",db_data)
        else:
            cursor.execute("INSERT INTO mails VALUES (?,?,?)", (mail,"", 0))


    @staticmethod
    async def check_imap_connection(mail):
        imap_user = mail[0]
        imap_password = mail[1]
        try:
            conn = imaplib.IMAP4_SSL("imap.{}".format(imap_user.split("@")[-1]))
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
            self.check_imap_connection(mail)
            await asyncio.sleep(0.01)

        print(success,len(mails)-success)

