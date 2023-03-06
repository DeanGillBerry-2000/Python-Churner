from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

# enter login information
userid = pyautogui.prompt("Please enter your AMEX username below (not the email associated with your account)")
password = pyautogui.password("Please enter your AMEX password below")

# login to the AMEX offers webpage
print("Beginning login sequence")
driver = webdriver.Chrome()
driver.get('https://global.americanexpress.com/offers')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'eliloUserID')))
userIDBox = driver.find_element(By.ID, 'eliloUserID')
userIDBox.send_keys(userid)
passwordBox = driver.find_element(By.ID, 'eliloPassword')
passwordBox.send_keys(password)
driver.find_element(By.ID, 'loginSubmit').click()

# detect the number of clickable offers
print("Login sequence complete. Waiting for offers page to load")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'filter-label-ALL')))
print("Web page has loaded, beginning search for credit card offers")
buttons = driver.find_elements(By.XPATH, '//button[@title = "Add to Card"]')

# if we actually have offers, start clicking them
if len(buttons) > 0:
    print('A total of '+str(len(buttons))+' offer(s) has been found. Beginning click process')
    count = 1
    for button in buttons:
        print('Clicking offer '+str(count)+' of '+str(len(buttons)))
        button.location_once_scrolled_into_view
        # we have to force a click, because it is sometimes hidden by the chat bubble
        driver.execute_script("arguments[0].click();", button)
        print('Offer '+str(count)+' clicked')
        count = count + 1
        # webpages need time to rest, otherwise we are going TOO fast
        time.sleep(1)
    print('All available offers on this webpage clicked')
# if there were no offers, print a message
else:
    print('No offers detected, please come back or try again later')
print('Closing applicaiton in 5 seconds')
time.sleep(5)
driver.close()

print('Thank you for using this application. Email imhoffnoah@gmail.com to report bugs and issues.')