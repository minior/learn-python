from selenium import webdriver
from selenium.webdriver.common.by import By # new step since Selenium 4
import time

# https://selenium-python.readthedocs.io/

browser = webdriver.Chrome()
browser.get("https://automatetheboringstuff.com/")
elements = browser.find_element(By.CSS_SELECTOR, "body > div > main > div > ul:nth-child(22) > li:nth-child(1) > a")
elements.click()
time.sleep(1)
elements = browser.find_elements(By.CSS_SELECTOR,'p') # finds paragraph elements
print(len(elements))

# input into web page:
browser.get("https://www.wikipedia.org/")
search_elem = browser.find_element(By.CSS_SELECTOR, '#searchInput') # searches for searchInput ID -> highlight & inspect element
search_elem.send_keys('Jerel Koh') # its me!!!!
search_elem.submit()
time.sleep(5)

# to read off a page:
browser.get("https://automatetheboringstuff.com/")
elements = browser.find_element(By.CSS_SELECTOR, "body > div > main > div > h2:nth-child(8)")
print(elements.text)

# other commands
browser.back()
browser.forward()
browser.refresh()
browser.quit()