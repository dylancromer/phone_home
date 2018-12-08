#!/usr/bin/python3

import os
from os.path import join, dirname
from dotenv import load_dotenv
import lib.pastebin as pastebin
import ip_tools

def main():
    """
    Writes data for paste on pastebin.com containing public and local IP addresses,
    then attempts to use the pastebin.com API to create the paste.
    """
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    pastebin_api_dev_key = os.environ.get("PASTEBIN_API_DEV_KEY")
    pastebin_api_user_key = os.environ.get("PASTEBIN_API_USER_KEY")

    api = pastebin.PasteBin(pastebin_api_dev_key, pastebin_api_user_key)

    ip_pub = ip_tools.get_public_ip()
    ip_loc = ip_tools.get_local_ip()

    data = 'public ip: ' + ip_pub + '\n' + 'local ip: ' + ip_loc

    result = api.paste(data, guest=False, name='whereami', private='1', expire='1H')

    if 'Bad API request' not in result:
        print('[+] - PasteBin URL: ' + result)
    else:
        raise SystemExit('[!] - Failed to create paste! ({0})'.format(result.split(', ')[1]))

if __name__ == '__main__':
    main()
