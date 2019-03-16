from phonehome.ip_tools import get_public_ip
from phonehome.flaregun import Flare
import daemon

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
