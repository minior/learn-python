import send2trash # avoids instant delete of os and shutil
import time

open('.\\13_files\\send2trashtest.txt', "w") # create file
time.sleep(3)
send2trash.send2trash('.\\13_files\\send2trashtest.txt') # deletes file