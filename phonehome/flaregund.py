from phonehome.ip_tools import get_public_ip
from phonehome.flaregun import Flare
import daemon

class FlareDaemon:
    def __init__(self, secret, dest_ip, link="https://twitter.com/dylanmcromer",
             delay=10, dest_port = 1331):

        self.secret = secret[0]
        self.dest_ip = dest_ip
        self.link = link
        self.delay = delay
        self.dest_port = dest_port

        flare_params = (self.link, self.delay, self.secret, self.dest_ip, self.dest_port)
        self.flare = Flare(*flare_params)

    def launch(self):
        self.flare.start_watching()

if __name__ == "__main__":
    LINK = "https://twitter.com/dylanmcromer"
    DELAY = 10
    SECRET = "trying to get a paper ready"
    DEST_IP = "127.0.0.1"
    DEST_PORT = 1321

    INIT_PARAMS = (LINK, DELAY, SECRET, DEST_IP, DEST_PORT)

    with daemon.DaemonContext():
        flare = Flare(INIT_PARAMS)
        flare.main_loop()
