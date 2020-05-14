import imaplib
import email
from configparser import ConfigParser

parser = ConfigParser()
parser.read('config.ini')

user = parser.get('account', 'email_adress')
password = parser.get('account', 'password')

imap_url = parser.get('general', 'imap_url')
mailbox = parser.get('email_config', 'email_box')

write_file = parser.get('general', 'std_write_file')

try:
    con = imaplib.IMAP4_SSL(imap_url)
except:
    print("Couldn't get to the IMAP server!")
    
print("currently in " + imap_url + " !")

try:
    con.login(user,password)
except:
    print("login failed!")
    exit(-1)

print("login successful!")
con.select(mailbox)

result, data = con.fetch(b'1','(RFC822)')
        
print(data)

with open(write_file,'w') as wf:
    wf.write(str(data))

exit(0)
