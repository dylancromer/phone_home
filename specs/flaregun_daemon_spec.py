"""
FLAREGUND

what does it do?
    - it spawns a flare for a secret
"""
from phonehome.flaregund import FlareDaemon
def test_daemon_starts_flare():
    failing_secret = ["ABCDEFGHijklmnop"]
    dest_ip = "127.0.0.1"

    fd = FlareDaemon(failing_secret, dest_ip)
    fd.launch()
    assert fd._panicked

"""
    - when the flare gets signalled and fires, it reloads with a new flare and the next secret in the rotation
    - it remembers which secrets are "used up"
    - if it gets low on secrets, it says so
"""
