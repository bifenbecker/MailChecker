import imaplib

class Connections:
    connections = []

    @staticmethod
    def get_connections(mail,passwd):
        print(mail,passwd)
        conn = imaplib.IMAP4_SSL("imap.{0}".format(mail.split("@")[-1]))

        try:
            conn.login(mail,passwd)
        except:
            conn = imaplib.IMAP4_SSL("imap.gmail.com")
            try:
                conn.login(mail,passwd)
            except:
                conn = None

        if conn is not None:
            Connections.connections.append(conn)