# last resort if no 3rd party direct-interaction modules avail
import pyautogui

print(pyautogui.size()) # screen res (0,0 is top left)
print(pyautogui.position()) #prints current mouse position
pyautogui.moveTo(100,100)
pyautogui.moveTo(1000,1000, duration=1)
pyautogui.moveRel(-200,-200, duration=0.5)
pyautogui.click(1128,759,duration=0.5) # clicks 19_ file
# can also use dragRel, doubleclick, rightclick etc.

# Note* failsafe to stop programme is to whip cursor to the top left

pyautogui.displayMousePosition() # also shows RGB values!
