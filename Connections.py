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
from email.header import decode_header

class Connections:
    main_window = None
    connections = []
    data_connections = []

    ALL_Accounts = 0
    CHCKED_Accounts = 0
    VALID_Accounts = 0
    UNVALID_Accounts = 0

    @staticmethod
    def get_connection(user: dict,path_session: str):
        f_good = open(os.path.join(path_session, 'GOOD.txt'), 'a')
        f_bad = open(os.path.join(path_session, 'BAD.txt'), 'a')
        f_remain = open(os.path.join(path_session, 'REMAIN.txt'), 'a')
        f_error = open(os.path.join(path_session, 'ERROR.txt'), 'a')
        Connections.ALL_Accounts += 1
        mail = user['mail']
        passwd = user['password']
        u = f"{mail}:{passwd}\n"
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
                f_error.write(u)

        if conn is not None:
            Connections.VALID_Accounts += 1
            f_good.write(u)
            conn.select()
            Connections.connections.append(conn)
            Connections.data_connections.append(user)
        else:
            Connections.UNVALID_Accounts += 1
            f_bad.write(u)

        f_good.close()
        f_bad.close()
        f_error.close()
        Connections.CHCKED_Accounts += 1
        Connections.Update_Date()

    @staticmethod
    def get_result_filter(table_req,requests = ()):
        for user_index in range(len(Connections.connections)):
            try:
                res, data = Connections.connections[user_index].search(None, *requests)
            except OSError:
                break
            except:
                continue
            item = QTreeItem.QTreeItem(data,Connections.connections[user_index])
            item.setText(0, Connections.data_connections[user_index]['mail'])
            item.setText(1, Connections.data_connections[user_index]['password'])
            item.setText(2, table_req)
            item.setText(3, str(len(data[0])))
            Connections.main_window.treeWidget.addTopLevelItem(item)

    @staticmethod
    def download_mail(conn,uid,path):
        try:
            result, email_data = conn.uid('fetch', uid, '(RFC822)')
            raw_email = email_data[0][1].decode("utf-8")
            email_message = email.message_from_string(raw_email)
            subject_ = Connections.decode(email_message['Subject'])
            date_ = Connections.scrap_date(str(email_message))

            counter = 1
            for part in email_message.walk():
                if part.get_content_maintype() == "multipart":
                    continue
                filename = part.get_filename()
                content_type = part.get_content_type()
                if not filename:
                    ext = mimetypes.guess_extension(content_type)
                    if not ext:
                        ext = '.bin'
                    if 'text' in content_type:
                        ext = '.txt'
                    if 'html' in content_type:
                        ext = '.html'
                    filename = 'msg-part-{}{}'.format(counter, ext)
                counter += 1

            non_symbols = ['/', ':', '*', '?', '"', '<', '>', '|']
            for symbol in non_symbols:
                if symbol in subject_:
                    subject_ = subject_.replace(symbol, ' ')
                if symbol in date_:
                    date_ = date_.replace(symbol, '.')

            save_path = os.path.join(path, date_, subject_)
            if not os.path.exists(save_path):
                os.makedirs(save_path)

            d_path = os.path.join(save_path, filename)
            with open(d_path, 'wb') as fp:
                fp.write(part.get_payload(decode=True))
        except:
            return -1




    @staticmethod
    def get_mail(conn,uid):
        try:
            result, email_data = conn.uid('fetch', uid, '(RFC822)')
            raw_email = email_data[0][1].decode("utf-8")
            email_message = email.message_from_string(raw_email)
            subject_ = Connections.decode(email_message['Subject'])
            date_ = Connections.scrap_date(str(email_message))
            to_ = Connections.decode(email_message['To'])
            from_ = Connections.decode(email_message['From'])

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
            mail = {'data': date_, 'from': from_, 'subject': subject_, 'content': content_, 'type': type}
            return mail
        except OSError:
            raise OSError
        except :
            return None

    @staticmethod
    def Update_Date():
        Connections.main_window.label_Accounts.setText(str(Connections.ALL_Accounts))
        Connections.main_window.label_Checked.setText(str(Connections.CHCKED_Accounts))
        Connections.main_window.label_Valid.setText(str(Connections.VALID_Accounts))
        Connections.main_window.label_Unvalid.setText(str(Connections.UNVALID_Accounts))

    @staticmethod
    def reset():
        Connections.data_connections = []
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
    def decode(s):
        if not s:
            return ""

        bytes_string, encoding = decode_header(s)[0]

        if encoding:
            s = bytes_string.decode(encoding)
        else:
            s = str(bytes_string)

        return s


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



