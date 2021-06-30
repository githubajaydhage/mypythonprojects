"""
@author: Manan
IF The code seems difficult to understand don't worry i have explained the code in detailed below after the code 
"""

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
import string
import time

browser = webdriver.ChromeOptions() #Chromedriver path.
browser.add_argument("start-maximized");
browser.add_argument("disable-infobars")
browser.add_argument("--disable-extensions")
browser = webdriver.Chrome(chrome_options=browser, executable_path=r'C:\Windows\chromedriver.exe') # <----- ENTER PATH HERE
browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher') #website you require to automate and run

sleep(2)

def start():
	username = browser.find_element_by_name('username')
	username.send_keys('_python_projects')
	password = browser.find_element_by_name('password')
	password.send_keys('Pythonprojects@123')
	nextButton = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
	nextButton.click()
	sleep(4)
	notification = browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
	notification.click()
	browser.get('https://www.instagram.com/explore/')
	


#Start the programm
start()