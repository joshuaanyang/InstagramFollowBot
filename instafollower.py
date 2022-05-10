from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = "/Users/JOSHUA/Downloads/chromedriver_win32/chromedriver.exe"

s = Service(chrome_driver_path)
op = webdriver.ChromeOptions()


USERNAME = "YOUR USERNAME"
P_USER = "YOUR PASSWORD"
SIMILAR_ACNT = "ACCOUNT TO FOLLOW"

user_x_path = '//*[@id="loginForm"]/div/div[1]/div/label/input'
pass_x_path = '//*[@id="loginForm"]/div/div[2]/div/label/input'
search_bar_x_path = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'
followers_list_x_path = '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div'


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=s, options=op)
        self.driver.get("https://www.instagram.com/")
        print("Instagram is now open.")

    def login(self):
        user = self.driver.find_element(By.XPATH, user_x_path)
        user.send_keys(USERNAME)
        pss = self.driver.find_element(By.XPATH, pass_x_path)
        pss.send_keys(P_USER)
        pss.send_keys(Keys.ENTER)

    def find_followers(self):
        search_bar = self.driver.find_element(By.XPATH, search_bar_x_path)
        search_bar.send_keys(SIMILAR_ACNT)
        time.sleep(3)
        search_bar.send_keys(Keys.ENTER)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(5)
        print("here")
        f = self.driver.find_element(By.XPATH, followers_list_x_path)
        f.click()
        time.sleep(10)

        # follows = self.driver.find_element(By.CSS_SELECTOR, ".isgrP .PZuss li button")
        # follows.click()

        follows = self.driver.find_elements(By.CSS_SELECTOR, ".isgrP .PZuss li button")
        for x in range(20):
            for follow in follows:
                if follow.text == "Following":
                    pass
                elif follow.text == "Requested":
                    pass
                elif follow.text == "Followed":
                    pass
                else:
                    follow.click()
        print("Done sir")
