"""
BOTTLE

what does it do:
    - it gets the external ip address
"""
from phonehome.ip_tools import get_public_ip
def test_public_ip_can_be_grabbed():
    ip = get_public_ip()
    assert ip is not None
    assert type(ip) is str
"""
- it waits for a signal
"""
from phonehome.bottle import check_url
def test_checks_for_secret_dont_fail_obviously():
    link = "https://twitter.com/dylanmcromer"

    word_that_is_always_there = "Dylan"
    assert check_url(link, word_that_is_always_there)

    word_that_is_never_there = "I hate Gary Bernhardt"
    assert not check_url(link, word_that_is_never_there)
"""
- when it sees that signal it send me the IP
"""
# tests need more work here - pretty hard!
