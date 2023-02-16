from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element_by_name("fName")
last_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
# sign_up = driver.find_element_by_css_selector(".btn-block")
sign_up = driver.find_element_by_css_selector("form button")
first_name.send_keys("")
last_name.send_keys("")
email.send_keys("")
# sign_up.send_keys(Keys.ENTER)
sign_up.click()
