from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

FB_EMAIL = ""
FB_PASSWORD = ""

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.com/")

login = driver.find_element_by_xpath('//*[@id="t-188693591"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()

sleep(2)
fb_button = driver.find_element_by_xpath('//*[@id="t-1917074667"]/main/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')
fb_button.click()

# Switch to facebook window and enter login details
sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email_input = driver.find_element_by_xpath('//*[@id="email"]')
password_input = driver.find_element_by_xpath('//*[@id="pass"]')

email_input.send_keys(FB_EMAIL)
password_input.send_keys(FB_PASSWORD)
password_input.send_keys(Keys.ENTER)

# Delay by 5 seconds to allow page to load
sleep(5)

# allow location, disallow notifications and allow cookies
location_popup = driver.find_element_by_xpath('//*[@id="t-1917074667"]/main/div/div/div/div[3]/button[1]')
notifications_popup = driver.find_element_by_xpath('//*[@id="t-1917074667"]/main/div/div/div/div[3]/button[2]/span')
cookies_popup = driver.find_element_by_xpath('//*[@id="t-188693591"]/div/div[2]/div/div/div[1]/div[1]/button/span')

location_popup.click()
notifications_popup.click()
cookies_popup.click()
