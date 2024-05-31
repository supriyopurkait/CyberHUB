import socket

def get_server_ip():
    hostname = socket.gethostname()
    server_ip = socket.gethostbyname(hostname)
    return server_ip