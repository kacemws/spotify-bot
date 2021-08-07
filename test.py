from selenium import webdriver
import os

from time import sleep

class Testin :
  def __init__(self):

    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", "180.252.181.3")
    profile.set_preference("network.proxy.http_port", "80")
    profile.update_preferences()

    self.driver = webdriver.Firefox(profile)

        
        
    self.driver.get("https://accounts.spotify.com/fr/login?continue=https:%2F%2Fopen.spotify.com%2Fplaylist%2F5l2svYsZfkevymEpv0lIv4")
        
    sleep(2)

    self.driver.find_element_by_xpath('//input[@name=\"username\"]')\
      .send_keys("test@mail.com")

        

    self.driver.find_element_by_xpath('//button[@id="login-button"]')\
      .click()


    sleep(30)

    self.driver.quit()

Testin()





