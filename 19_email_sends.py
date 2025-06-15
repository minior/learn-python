# use-case: send self email to serve as event notification eg. price etc.
import smtplib
connection_obj = smtplib.SMTP('smtp.gmail.com', 587) #usually default
print(type(connection_obj))

conn = connection_obj
conn.ehlo() # establishes connection
print(conn.ehlo()) # shows server return code -> 250 is good
conn.starttls() # start TLS encryption
conn.login('email add', 'password') # *Note: good to generate google's APP SPECIFIC PASSWORDS for security
conn.sendmail('from email(mine)', 'target email', 'Subject: <subject> \n\n <all body text inc newlines>') 
# we can create a recipients = [] list to send to multiple recipients
# returns a dictionary {} of FAILED sends (blank is good)
conn.quit()
connection_obj.quit()
