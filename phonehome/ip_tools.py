#!/usr/bin/env python3

import socket
from requests import get

def get_local_ip():
    """
    No arguments, returns local IP as string.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("8.8.8.8", 80))
    local_ip = sock.getsockname()[0]
    sock.close()

    return local_ip

def get_public_ip():
    """
    No args, returns public IP as string.
    """
    public_ip = get('https://api.ipify.org').text
    return public_ip

if __name__ == '__main__':
    LOCAL = get_local_ip()
    print(LOCAL)
    PUBLIC = get_public_ip()
    print(PUBLIC)
