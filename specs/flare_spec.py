"""
FLARE

what does it do:
    - it gets the external ip address
"""
from phonehome.ip_tools import get_public_ip
def test_public_ip_can_be_grabbed():
    ip = get_public_ip()
    assert ip is not None
    assert type(ip) is str
"""
    - it looks for a signal
"""
from phonehome.flaregun import Flare
def test_checks_for_secret_dont_fail_obviously():
    link = "https://twitter.com/dylanmcromer"
    word_that_is_always_there = "Dylan"

    flare = Flare(link, 10, word_that_is_always_there, '127.0.0.1', 1331)
    assert flare.check_url()

    word_that_is_never_there = "I hate Gary Bernhardt"

    flare = Flare(link, 10, word_that_is_never_there, '127.0.0.1', 1331)
    assert not flare.check_url()
"""
    - when it sees that signal it send me the IP
"""
# tests need more work here - pretty hard!
"""
    - tries again if it can't connect the first time, then puts itself into a panic state and retries every 5 minutes
"""
def test_retry_connection():
    link = "https://twitter.com/dylanmcromer"
    word_that_is_always_there = "Dylan"

    flare = Flare(link, 10, word_that_is_always_there, '127.0.0.1', 1331)
    assert flare._panic_cannot_send_flare(test=True)
