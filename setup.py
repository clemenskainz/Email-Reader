from configparser import ConfigParser

wr_file = ""
config = ConfigParser()

config['account'] = {
    'email_adress': '',
    'password': '',
}
config['general'] = {
    'imap_url': 'imap.gmail.com',
    'std_write_file': 'mail_save.txt'
    }
config['email_config'] = {
    'email_box': 'INBOX'
    }
config['admins'] = {
    'admin0': '',
    'admin1': '',
    'admin2': ''
    }
config['white_list'] = {
    '0': '',
    '1': '',
    '2': '',
    '4': '',
    '5': '',
    '6': '',
    '7': '',
    '8': '',
    '9': ''
    }
config['black_list'] = {
    '0': '',
    '1': '',
    '2': '',
    '4': '',
    '5': '',
    '6': '',
    '7': '',
    '8': '',
    '9': ''
    }

with open('config.ini', 'w') as f:
    config.write(f)

with open('mail_save.txt', 'w') as s:
    pass

with open('Main.py', 'w') as py:
    config.write("""
import imaplib
import email
from configparser import ConfigParser

parser = ConfigParser()
parser.read('config.ini')""")
