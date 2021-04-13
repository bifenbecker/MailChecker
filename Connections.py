import imaplib
import json
import os
from threading import *

class Connections:
    main_window = None
    connections = []

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
            Connections.connections.append(conn)
        else:
            Connections.UNVALID_Accounts += 1

        Connections.CHCKED_Accounts += 1
        Connections.Update_Date()


    @staticmethod
    def get_result_filter(request: str):
        pass

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
    def load_main_window(window):
        Connections.main_window = window



