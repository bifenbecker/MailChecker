import socket


def run_check():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False





