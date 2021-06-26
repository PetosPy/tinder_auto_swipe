from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
import time

EMAIL = "YourEmail"
PASSWORD = "password"
webdriver_path = "C:/development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=webdriver_path) 
driver.get("https://tinder.com/")

# Press the login button
time.sleep(20)
login_button = driver.find_element_by_xpath('//*[@id="u2005023502"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
time.sleep(3)
login_button.click()

# Selecting Facebook as login option
time.sleep(5)
fb_login = driver.find_element_by_xpath('//*[@id="u276642426"]/div/div/div[1]/div/div[3]/span/div[2]/button')
time.sleep(1)
fb_login.click() 

# switching to the popUp window for login
time.sleep(10)
driver.window_handles
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

#Logging into facebook
time.sleep(10)
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys(EMAIL)

time.sleep(2)
password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

# Location prompt
driver.switch_to.window(base_window)
time.sleep(15)
enable_location = driver.find_element_by_xpath('//*[@id="u276642426"]/div/div/div/div/div[3]/button[1]')
time.sleep(5)
enable_location.click()

time.sleep(2)
notification_button = driver.find_element_by_xpath('//*[@id="u276642426"]/div/div/div/div/div[3]/button[1]')
time.sleep(5)
notification_button.click()
print("Passed location")

# Accept cookies
time.sleep(5)
accept_cookies = driver.find_element_by_xpath('//*[@id="u2005023502"]/div/div[2]/div/div/div[1]/button')
accept_cookies.click() 


time.sleep(10)
like_button = driver.find_element_by_xpath('//*[@id="u2005023502"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[4]/div/div[4]/button/span/span')


likes = 0
while likes < 20:
	try:
		time.sleep(2)
		like_button.click()
		likes +=1
	except ElementClickInterceptedException:
		webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
	else:
		time.sleep(2)
		like_button.click()
		likes +=1



print("Done liking")