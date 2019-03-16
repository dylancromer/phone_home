import sys
import socket
import requests
import time
from phonehome.ip_tools import get_public_ip

class FlareNotSentError(Exception):
        def __init__(self, message):
            self.message = message

class Flare(object):
    def __init__(self, link, delay, secret, dest_ip, dest_port):
        self.link, self.delay, self.secret, self.dest_ip, self.dest_port = link, delay, secret, dest_ip, dest_port

    def _get_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.dest_ip, self.dest_port))
        return sock

    def send_ip(self):
        try:
            sock = self._get_socket()
        except ConnectionRefusedError as e:
            try:
                sock = self._get_socket()
            except ConnectionRefusedError as e:
                raise FlareNotSentError(f"Flare encountered the following error and could not be sent: {e}")

        source_ip = get_public_ip()
        payload = bytearray(source_ip, 'utf8')
        sock.send(payload)

    def check_url(self):
        page = requests.get(self.link)

        if self.secret in page.text:
            return True
        else:
            return False

    def _panic_cannot_send_flare(self, test=False):
        monitor_interval = 5*60
        self._panicked = True

        while self._panicked:
            try:
                self.send_ip()
                self._panicked = False
            except FlareNotSentError:
                if not test:
                    time.sleep(monitor_interval)
                    continue
                else:
                    return self._panicked

    def main_loop(self):
        print("Flare ready to be fired.")
        while True:
            if not self.check_url():
                time.sleep(self.delay)
            else:
                try:
                    self.send_ip()
                except FlareNotSentError:
                    self._panic_cannot_send_flare()
                finally:
                    break


    def start_watching(self):
        self.main_loop()
