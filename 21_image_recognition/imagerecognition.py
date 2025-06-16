import pyautogui, os, time

print(type(pyautogui.screenshot())) # returns PILLOW image module object
pyautogui.screenshot('21_image_recognition\\screenshot_example.jpeg')

os.startfile("21_image_recognition\\screenshot_example.jpeg") # open screenshot)
time.sleep(2)
print(pyautogui.locateOnScreen("21_image_recognition\\image_recognition_source.jpg", confidence=0.8)) # locates settings icon (x,y,source size)
print('\n' + str(pyautogui.locateCenterOnScreen("21_image_recognition\\image_recognition_source.jpg", confidence=0.8))) # locates center of found box
width, height = pyautogui.locateCenterOnScreen("21_image_recognition\\image_recognition_source.jpg", confidence=0.8)
pyautogui.moveTo(width, height, duration=0.5) # move to the found image

# *Note: Locates are COMPUTATIONALLY EXPENSIVE, and very strict (hence confidence)

pyautogui.click()
pyautogui.hotkey('alt', 'f4') #close image window
