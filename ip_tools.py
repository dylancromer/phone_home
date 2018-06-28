import socket
from requests import get
from ipgetter import myip

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()

    return local_ip

def get_public_ip_simple():
    ip = get('https://api.ipify.org').text
    return ip

def get_public_ip():
    return myip()

if __name__ == '__main__':
    local = get_local_ip()
    print(local)
    public = get_public_ip()
    print(public)
