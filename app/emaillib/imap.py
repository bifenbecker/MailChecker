import base64
import mimetypes
import imaplib
import email
import time


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

        date = date.split(' ')[:5]
        time_obj = time.strptime(' '.join(date), '%a, %d %b %Y %H:%M:%S')

        return int(time.mktime(time_obj))

    @staticmethod
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
            message = {}

            result, email_data = self.connection.uid('fetch', item, '(RFC822)')
            raw_email = email_data[0][1].decode("latin-1")
            msg = email.message_from_string(raw_email)

            result = ""
            for part in msg.walk():

                if part["Content-Type"].startswith('text/html'):
                    result = part
                    break

                elif part["Content-Type"].startswith('text/plain'):
                    result = part

                if part.get_content_maintype() == 'multipart':
                    continue

            message["date"] = self.get_unix_time(str(msg["Date"]))
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
