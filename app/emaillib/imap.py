import time

import mimetypes
import imaplib

import email
from email.header import decode_header


class IMAP:
    """IMAP4 client class.

    Class provides opportunities to create connection with imap server
    and receive mails from email account.

    address - email address for connection
    password - email password for connection
    server - imap server address (default: "")
    secure - connection secure mode (default: False)"""

    def __init__(self, address: str, password: str, server: str = "", secure: bool = False):
        self.messages = []

        if not server:
            server = f"imap.{address.split('@')[-1]}"

        if secure:
            self.connection = imaplib.IMAP4_SSL(server)
        else:
            self.connection = imaplib.IMAP4(server)

        try:
            self.connection.login(address, password)
        except imaplib.IMAP4.error as err:
            if "[AUTHENTICATIONFAILED]" in str(err):
                raise Error("Authentication failed")
            else:
                raise imaplib.IMAP4.error(err)

    @staticmethod
    def get_unix_time(date: str) -> int:
        """Convert date to unix-time

        date can only have '%a, %d %b %Y %H:%M:%S' format"""

        # print(date)

        if date[:1].isdigit():
            date = date.split()[:4]
        else:
            date = date.split()[1:5]

        time_obj = time.strptime(' '.join(date), '%d %b %Y %H:%M:%S')

        return int(time.mktime(time_obj))

    @staticmethod
    def _clear_subject(subject: str) -> str:
        """Clear subject field in imap response

        subject - string, that will be cleared"""

        bytes_string, encoding = decode_header(subject)[0]

        if encoding:
            subject = bytes_string.decode(encoding)
        else:
            subject = str(bytes_string)

        return subject

    @staticmethod
    def get_filter(query_params: dict):
        """Create and return IMAP query to select certain messages

        query_params - dict of fields, which shall be used to create query"""

        query = ""

        if query_params["new"]:
            query += "NEW "

        if query_params["in_header"] and query_params["in_body"]:
            query += f"TEXT \"{query_params['string']}\" "
        elif query_params["in_header"]:
            query += f"HEADER \"{query_params['string']}\" "
        elif query_params["in_body"]:
            query += f"BODY \"{query_params['string']}\" "

        if query_params["since"]:
            query += f"SINCE {query_params['since']}"
        elif query_params["before"]:
            query += f"BEFORE {query_params['before']}"
        elif query_params["on"]:
            query += f"ON {query_params['on']}"

        query_list = query.split()
        if len(query_list) == 1:
            return query_list[0]
        elif len(query_list) > 1:
            return f"({query})"
        else:
            return "ALL"

    def get_uids(self, folder: str = "INBOX", _filter: str = "ALL", _from: int = 0, _to: int = 0) -> list:
        """Get uid's(special id's) of messages with certain filter

        folder - folder on imap server, which will be selected (default: "INBOX")
        _filter - filter to select messages (default: "ALL")
        _from - lower frame of selection (default: 0)
        _to - upper frame of selection (default: 0)"""

        self.connection.select(folder)
        result, data = self.connection.uid('search', None, _filter)
        uids_list = data[0].split()

        if not _to:
            _to = len(uids_list)

        return uids_list[_from:_to]

    def get_message(self, uid: bytes) -> dict:
        """Get message from email address

        uid - id of message to receive certain message"""

        message = {}

        result, email_data = self.connection.uid('fetch', uid, '(RFC822)')
        raw_email = email_data[0][1].decode("latin-1")
        msg = email.message_from_string(raw_email)

        # msg = email.message_from_bytes(email_data[0][1])

        result = ""
        flag = True

        for part in msg.walk():

            content_type = part.get_content_type()

            if 'multipart' in content_type:
                continue

            if content_type == 'text/html':
                result = part
                break

            elif flag and content_type == 'text/plain':
                result = part
                flag = False

        # print(_structure(msg))
        # print(result)
        # print(msg["Delivery-date"])
        # message["date"] = self.get_unix_time(msg["Received"].split('; ')[-1])

        # message["date"] = self.get_unix_time(msg["Date"])
        message["sender"] = msg["From"]
        message["subject"] = self._clear_subject(msg["Subject"])
        message["content"] = str(result.get_payload(decode=True))
        message["content_extension"] = mimetypes.guess_extension(result.get_content_type())

        # message["raw_message"] = msg
        # message["structure"] = _structure(msg)

        if message not in self.messages:
            self.messages.append(message)

        return message

    def get_messages(self, uids_list: list) -> list:
        """Get messages from email address and fill messages field of IMAP instance

        uids_list - list of messages id's to receive messages"""

        messages = []

        for uid in uids_list:

            print('message uid: ', uid)

            message = self.get_message(uid)
            messages.append(message)

        return messages


class Error(Exception):
    """Error class for generating exceptions for IMAP class"""

    def __init__(self, text):
        self.text = text
