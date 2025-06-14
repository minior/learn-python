#! python3
import re, pyperclip

# GOAL is to be able to copy entire documents, run the code, and be able to paste a 
# list of emails, and singapore phone numbers

#regex for nums *note that ?: means treat as non-capturing group
phone_regex = re.compile(r'''
# 9000 0000, #90000000, (+)65 9000 0000, 659000000, 65 90000000     
(?:\+?   # optional plus sign
\d{2}    # optional area code 2 digits
\s{,1})? # optional space
\d{4}    # 4 digits
\s{,1}   # optional space
\d{4}    # 4 digits ''', re.VERBOSE)

#regex for emails
email_regex = re.compile(r'''
#some._+thing@something.thing
[a-z0-9_.+]{1,}     # name
@                   # @ symbol
[a-z0-9_.+]{1,}     # domain 
''', re.VERBOSE | re.I)

#clear / paste clipboard
text = pyperclip.paste()

#get matches
matched_phone = phone_regex.findall(text)
matched_email = email_regex.findall(text)
print(matched_phone)
print(matched_email)

#copy to clipboard, use "\n".join to combine lists, separating each item with \n
results = "\n".join(matched_phone) + "\n" + "\n".join(matched_email) 
print(results)
pyperclip.copy(results)