import lib.pastebin as pastebin
import os
from os.path import join, dirname
from dotenv import load_dotenv
import ip_tools

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

PASTEBIN_API_DEV_KEY = os.environ.get("PASTEBIN_API_DEV_KEY")
PASTEBIN_API_USER_KEY = os.environ.get("PASTEBIN_API_USER_KEY")

api = pastebin.PasteBin(PASTEBIN_API_DEV_KEY, PASTEBIN_API_USER_KEY)

ip_pub = ip_tools.get_public_ip()
ip_loc = ip_tools.get_local_ip()

data = 'public ip: ' + ip_pub + '\n' + 'local ip: ' + ip_loc

result = api.paste(data, guest=False, name='whereami', private='1', expire='10M')
if 'Bad API request' not in result:
        print('[+] - PasteBin URL: ' + result)
else:
        raise SystemExit('[!] - Failed to create paste! ({0})'.format(api_user_key.split(', ')[1]))

