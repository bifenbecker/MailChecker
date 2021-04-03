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
        except Exception:
            raise Error("Authentication failed")

    @staticmethod
    def get_unix_time(date: str) -> int:
        """Convert date to unix-time

        date can only have '%a, %d %b %Y %H:%M:%S' format"""

        print(date)

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

    def get_messages(self, folder: str = "INBOX", _filter: str = "ALL", _from: int = 0, _to: int = 0) -> list:
        """Get messages from email address and fill messages field of IMAP instance

        folder - folder on imap server, which will be selected (default: "INBOX")
        _filter - filter to select messages (default: "ALL")
        _from - lower frame of selection (default: 0)
        _to - upper frame of selection (default: 0)"""

        self.connection.select(folder)

        result, data = self.connection.uid('search', None, _filter)
        item_list = data[0].split()

        if not _to:
            _to = len(item_list)

        for item in item_list[_from:_to]:

            print('message: ', item_list.index(item))

            message = {}

            result, email_data = self.connection.uid('fetch', item, '(RFC822)')
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
            message["date"] = self.get_unix_time(msg["Received"].split('; ')[-1])
            message["sender"] = msg["From"]
            message["subject"] = self._clear_subject(msg["Subject"])
            message["content"] = str(result.get_payload(decode=True))
            message["content_extension"] = mimetypes.guess_extension(result.get_content_type())

            # message["raw_message"] = msg
            # message["structure"] = _structure(msg)

            if message not in self.messages:
                self.messages.append(message)

        return self.messages


class Error(Exception):
    def __init__(self, text):
        self.text = text
