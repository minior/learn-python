import pyautogui

# type into terminal!
pyautogui.click(1400,500,duration=0.5)
pyautogui.typewrite("hello!", interval=0.1)

# we can run multiple lines from INTERACTIVE SHELL using ;
pyautogui.click(1400,500,duration=0.5); pyautogui.typewrite("echo('hello!!!')",interval=0.1)

# what about shift, enter, arrow keys etc.?
pyautogui.click(1400,500, duration=0.5)
pyautogui.typewrite(['a', 'B', 'enter', 'X'], interval=0.1)

# list of keys: 
# print(pyautogui.KEYBOARD_KEYS)

# for shortcuts
for i in range(7):
    pyautogui.hotkey('ctrl', 'z') 