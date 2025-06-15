import webbrowser # module
import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)
print(res.text[:100])

# to crash the program incase of a bad download
res.raise_for_status()
badres = requests.get('https://automatetheboringstuff.com/files/asdkl;hjfakldfhj')
badres.raise_for_status() 

# to download a web file, pass "wb" keyword arg to .open()
testwebpage = requests.get('https://automatetheboringstuff.com/files/rj.txt')
testdownload = open(testwebpage, "wb") # wb = web binary
# download part
for bytechunk in res.iter_content(100000):
    testdownload.write(bytechunk)

#webbrowser.open('https://youtube.com')

