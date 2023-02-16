from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

USERNAME = ""
PASSWORD = ""

chrome_driver = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver)
url = "https://www.linkedin.com/jobs/search/?currentJobId=3204243375&f_AL=true&geoId=102713980&keywords=python%20developer&location=India&refresh=true"
driver.get(url)

# Login
login = driver.find_element_by_class_name("btn-secondary-emphasis")
login.click()

time.sleep(5)

username_input = driver.find_element_by_id("username")
username_input.send_keys("")
password_input = driver.find_element_by_id("password")
password_input.send_keys(PASSWORD)
sign_in_btn = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
sign_in_btn.send_keys(Keys.ENTER)

# Save and follow
save_btn = driver.find_element_by_class_name("jobs-save-button")
save_btn.click()
