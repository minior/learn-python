import imapclient

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True) # use ssl encryption
conn.login('email add', 'password') # returns "email authenticated (Success)"
print(conn.list_folders) # folder name will be third entry in each tuple
conn.select_folder('INBOX', readonly=True) # set readonly to prevent unintentional deletes
Unique_IDs = conn.search(['SINCE 05-AUG-2015']) # syntax is weird, use documentation
print(Unique_IDs)
#returns list of UIDs corresponding to individual emails
raw_message = conn.fetch(['uid_number'], ['BODY[]', 'FLAGS[]'])
#returns lots of irrelevant info

#parse with pyzmail (now maybe outdated)
import pyzmail
message_object = pyzmail.PyzMessage.factory(raw_message['uid_number'][b'BODY[]'])
message_object.get_addresses('from')
print(message_object.text_part) #(check)
message_object.text_part.get_payload().decode('UTF-8')

# IMAP SEARCH KEYS:
# https://automatetheboringstuff.com/2e/chapter18/#calibre_link-1113

# Deleting Messages
conn.select_folder('INBOX', readonly=False)
UIDs = conn.search(['IMAP SEARCH'])
print(UIDs)
conn.delete_messages(['UID'])
