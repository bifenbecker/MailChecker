import base64
import email
import imaplib,QTreeItem
import json
import mimetypes
import os
import re
from threading import *
from multiprocessing.pool import ThreadPool
from PyQt5.QtCore import QDate


class Connections:
    main_window = None
    connections = []
    data_connections = []

    ALL_Accounts = 0
    CHCKED_Accounts = 0
    VALID_Accounts = 0
    UNVALID_Accounts = 0

    @staticmethod
    def get_connection(user: dict):
        Connections.ALL_Accounts += 1
        mail = user['mail']
        passwd = user['password']
        server = "imap.{0}".format(mail.split("@")[-1])
        try:
            conn = imaplib.IMAP4_SSL(server)
            conn.login(mail,passwd)
        except:
            conn = imaplib.IMAP4_SSL("imap.gmail.com")
            try:
                conn.login(mail,passwd)
            except:
                conn = None

        if conn is not None:
            Connections.VALID_Accounts += 1
            conn.select()
            Connections.connections.append(conn)
            Connections.data_connections.append(user)
        else:
            Connections.UNVALID_Accounts += 1

        Connections.CHCKED_Accounts += 1
        Connections.Update_Date()

    @staticmethod
    def get_result_filter(requests = ()):
        for user_index in range(len(Connections.connections)):
            res,data = Connections.connections[user_index].search('windows-1251',*requests)
            item = QTreeItem.QTreeItem(data,Connections.connections[user_index])
            item.setText(0, Connections.data_connections[user_index]['mail'])
            item.setText(1, Connections.data_connections[user_index]['password'])
            item.setText(2, 'REQ')#
            item.setText(3, str(len(data[0])))
            Connections.main_window.treeWidget.addTopLevelItem(item)

    @staticmethod
    def get_mail(conn,uid):
        try:
            result, email_data = conn.uid('fetch', uid, '(RFC822)')
            raw_email = email_data[0][1].decode("utf-8")  # str
            email_message = email.message_from_string(raw_email)  # email.message.Message
            subject_ = email_message['Subject']
            from_ = email_message['From']
            data_ = email_message['Date']
            data_ = Connections.scrap_date(str(email_message))

            if "=?UTF-8?B?" in subject_:
                subject_ = ""
                for subject in email_message['Subject'].split('=?UTF-8?B?'):
                    subject_ += base64.b64decode(subject).decode('utf-8')
            if "=?utf-8?B?" in subject_:
                subject_ = ""
                for subject in email_message['Subject'].split('=?utf-8?B?'):
                    subject_ += base64.b64decode(subject).decode('utf-8')

            if "=?UTF-8?B?" in from_:
                from_ = ""
                for f in email_message['From'].split('=?UTF-8?B?'):
                    from_ += base64.b64decode(f).decode('utf-8')
            if "=?utf-8?B?" in from_:
                from_ = ""
                for f in email_message['From'].split('=?utf-8?B?'):
                    from_ += base64.b64decode(f).decode('utf-8')

            result = ""
            flag = True

            for part in email_message.walk():
                content_type = part.get_content_type()
                if 'multipart' in content_type:
                    continue
                if content_type == 'text/html':
                    result = part
                    break
                elif flag and content_type == 'text/plain':
                    result = part
                    flag = False
                elif flag:
                    result = part
            type = mimetypes.guess_extension(result.get_content_type())
            content_ = part.get_payload(decode=True)
            mail = {'data': data_, 'from': from_, 'subject': subject_, 'content': content_, 'type': type}
            return mail
        except:
            return None

    @staticmethod
    def Update_Date():
        Connections.main_window.label_Accounts.setText(str(Connections.ALL_Accounts))
        Connections.main_window.label_Checked.setText(str(Connections.CHCKED_Accounts))
        Connections.main_window.label_Valid.setText(str(Connections.VALID_Accounts))
        Connections.main_window.label_Unvalid.setText(str(Connections.UNVALID_Accounts))

    @staticmethod
    def reset():
        Connections.connections = []
        Connections.ALL_Accounts = 0
        Connections.CHCKED_Accounts = 0
        Connections.UNVALID_Accounts = 0
        Connections.VALID_Accounts = 0

    @staticmethod
    def parse_date(date: QDate):
        day = date.day()
        if day < 10:
            day = f"0{day}"
        else:
            day = str(day)
        month = date.month()
        year = date.year()
        str_month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        return f"{day}-{str_month[month-1]}-{year}"

    @staticmethod
    def scrap_date(message: email) -> str:

        if not message:
            return ""

        pattern = r'.?\d [A-Z][a-z]{2} \d{4} (\d{2}:){2}\d{2}'
        result = re.search(pattern, message)

        return result.group(0) if result else ""

    @staticmethod
    def load_main_window(window):
        Connections.main_window = window



