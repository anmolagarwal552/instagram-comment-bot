from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
#----------------------------------
file = open('com.txt','r')
file = file.readlines()
com = []
for i in file:
    com.append(i)
#----------------------------------
noc = open('noc.txt','r')
noc = noc.readlines()
noc1 = 0
for nocx in noc:
    noc1 = noc1 + int(nocx)
#----------------------------------
dt = open('dt.txt','r')
dt = dt.readlines()
dt1 = 0
for dtx in dt:
    dt1 = dt1 + int(dtx)
#----------------------------------
cmt = open('link.txt','r')
cmt = cmt.readlines()
commt = ""
for j in cmt:
    commt = commt + j
#----------------------------------
class InstaBots:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()
    
    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)
        email= bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        ctr = 0
        for comm in com:
            bot.get(commt)
            entry = lambda: bot.find_element_by_xpath("//textarea[@aria-label='Add a comment…']")
            entry().click()
            entry().clear()
            entry().send_keys(random.choice(com))
            time.sleep(dt1)
            entry().send_keys(Keys.ENTER)
            ctr += 1
            if ctr == noc1:
                bot.get(commt)
                time.sleep(4)
                bot.close()
obj = InstaBots('username','password')
obj.login()
