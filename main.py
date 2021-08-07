from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

from time import sleep
import random

def sleep_random(num) :
    sleep((random.random() * 10) % num)

class SpotifyBot :
    def __init__(self,email,email2,password, proxyip, proxyport,followed):

        profile = webdriver.FirefoxProfile()
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", proxyip)
        profile.set_preference("network.proxy.http_port", proxyport)
        profile.update_preferences()

        
        self.driver = webdriver.Firefox(profile) 
        self.driver2 = webdriver.Firefox(profile)
        

        # self.driver = webdriver.Chrome()

        
        self.driver.get("https://accounts.spotify.com/fr/login?continue=https:%2F%2Fopen.spotify.com%2Fplaylist%2F5l2svYsZfkevymEpv0lIv4")
        self.driver2.get("https://accounts.spotify.com/fr/login?continue=https:%2F%2Fopen.spotify.com%2Fplaylist%2F5l2svYsZfkevymEpv0lIv4")
        sleep_random(3)

        self.driver.find_element_by_xpath('//input[@name=\"username\"]')\
            .send_keys(email)

        self.driver2.find_element_by_xpath('//input[@name=\"username\"]')\
            .send_keys(email2)
        
        sleep_random(2)
        self.driver.find_element_by_xpath('//input[@name=\"password\"]')\
            .send_keys(password)
        self.driver2.find_element_by_xpath('//input[@name=\"password\"]')\
            .send_keys(password)
        sleep_random(2)

        self.driver.find_element_by_xpath('//button[@id="login-button"]')\
            .click()
        self.driver2.find_element_by_xpath('//button[@id="login-button"]')\
            .click()

        sleep(30)

        if(followed == False):
            # self.driver.find_element_by_xpath('//button[@title="Sauvegarder dans Bibliothèque"]')\
            #     .click()
            element = self.driver.find_element_by_class_name("spoticon-heart-32")
            self.driver.execute_script("arguments[0].click();", element) 
            element = self.driver2.find_element_by_class_name("spoticon-heart-32")
            self.driver2.execute_script("arguments[0].click();", element)
            # //equivalent
        else:
            print("already a follower")

        # sleep_random(5)

        # element = self.driver.find_element_by_class_name("_11f5fc88e3dec7bfec55f7f49d581d78-scss")
        # self.driver.execute_script("arguments[0].click();", element) 
        # element = self.driver2.find_element_by_class_name("_11f5fc88e3dec7bfec55f7f49d581d78-scss")
        # self.driver2.execute_script("arguments[0].click();", element) 
        sleep_random(20)
        # self.driver.find_element_by_xpath('//button[@title="Lecture"]')\
            # .click()
        # self.driver2.find_element_by_xpath('//button[@title="Lecture"]')\
            # .click()

        sleep_random(10)
        # self.driver.find_element_by_xpath('//button[@title="Pause"]')\
        #     .click()
        # sleep(2)
        self.driver.quit()
        self.driver2.quit()



password = 'password'
emails = [
    "aaphlbfk@gmail.com",
    "hiwvayaa@gmail.com",
    "yeoeehur@gmail.com",
    "dsbmgkia@gmail.com",
    "dndtbdyp@gmail.com",
    "hnakqbzp@gmail.com",
    "lmdysonz@gmail.com",
    "lkveficm@gmail.com",
    "efrwjxce@gmail.com",
    "fbbpbgmb@gmail.com"
]
proxyip = [
    "41.72.196.49",
    "190.11.15.14",
    "104.248.158.243",
    "167.71.5.83",
    "159.203.61.169",
    "191.240.152.130",
    "201.184.130.194",
    "12.139.101.100",
    "176.9.75.42",
    "121.33.220.158",
    "66.96.237.86",
    "34.222.24.128",
    "95.71.125.50",
    "89.22.23.57",
    "200.73.128.86",
    "122.154.72.102",
    "201.59.214.82",
    "5.22.154.50",
    "128.199.202.122",
]
proxyport = [
    "8080",
    "55443",
    "44344",
    "3128",
    "3128",
    "80",
    "51406",
    "80",
    "3128",
    "808",
    "8080",
    "3128",
    "49882",
    "80",
    "80",
    "8080",
    "8080",
    "34895",
    "3128"
]

print("\n",len(emails))
for index in range(len(emails)) : 
    #if we have a pair number of emails, we will pass 2 of them together, 
    #if not, we will pass 2 of them together in condition that we are not passing the last number with them : 
    #11 emails : 1-2 3-4 5-6 7-8 9-10 and 11 is alone
    proxy_index = random.randint(0,len(proxyip)-1)
    if(len(emails) %2 == 0) : 
        if(index%2 == 0) : 
            SpotifyBot(emails[index],emails[index+1],'password',proxyip[proxy_index],proxyport[proxy_index],False)
    else:
        if(index == len(emails) - 1 ) : 
            print(index)
        else : 
            if(index%2 == 0) : 
                print(str(index)+" and "+str(index+1))

# for email in emails : 
#     proxy_index = random.randint(0,len(proxyip)-1)
#     SpotifyBot(email,'password',proxyip[proxy_index],proxyport[proxy_index],False)
