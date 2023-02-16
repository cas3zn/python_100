from selenium import webdriver
from time import *

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = 'C://Development/chromedriver.exe'
TWITTER_EMAIL = ''
TWITTER_PASSWORD = ''


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')

        sleep(3)
        start_btn = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]'
        )
        start_btn.click()

        sleep(60)
        self.down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]'
            '/div/div/div[2]/div[1]/div[1]/div/div[2]/span'
        )
        self.up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]'
            '/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
        )

        print(f'down: {self.down}\nup: {self.up}')

        self.driver.quit()


    def tweet_at_provider(self):
        pass


twitter_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()