import webbrowser
import requests

# to download a web file, pass "wb" keyword arg to .open()

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
testdownload = open('15_testwebdownload.txt', "wb") # wb = web binary
# download part
for bytechunk in res.iter_content(100000):
    testdownload.write(bytechunk)

#webbrowser.open('https://youtube.com')
