#!/usr/bin/env python
# coding: utf-8

# # DDR Assignment 4
# 
# ### Leyla Dong

# In[1]:


from bs4 import BeautifulSoup
import requests
import urllib
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
from selenium.webdriver.common.keys import Keys
import time
import webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest


# (1) please get Selenium to work on your system.  I.e., try to code something up in Java or Python that starts a browser of your choice, navigates to google.com, and searches for "askew" as well as "google in 1998" (separate searches!)

# In[2]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='/Applications/chromedriver')
driver.implicitly_wait(10)
driver.set_script_timeout(120)
driver.set_page_load_timeout(10)
driver.get("https://google.com");
inp = driver.find_element_by_css_selector("input[type=text]")
inp.send_keys("askew\n")
time.sleep (5)
driver.execute_script("window.open('http://google.com');")
driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(10)
driver.find_element_by_name('q').send_keys('google in 1998\n')
time.sleep (5)
driver.quit()


# (2) write a script that goes to bestbuy.com, clicks on Deal of the Day, reads how much time is left for the Deal of the Day and prints the remaining time to screen (console), clicks on the Deal of the Day (the actual product), clicks on its reviews, and saves the resulting HTML to your local hard drive as "bestbuy_deal_of_the_day.htm"

# In[3]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
import codecs
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path='/Applications/chromedriver')
driver.implicitly_wait(10)
driver.set_script_timeout(120)
driver.set_page_load_timeout(30)
driver.get("https://www.bestbuy.com/")
driver.implicitly_wait(5)

deal = driver.find_element_by_xpath(".//*[contains(text(), 'Deal of the Day')]")
deal.click()
time.sleep(2)

Hour = driver.find_element_by_css_selector("span[class='hours cdnumber']").text
Min = driver.find_element_by_css_selector("span[class='minutes cdnumber']").text
Sec = driver.find_element_by_css_selector("span[class='seconds cdnumber']").text
driver.implicitly_wait(5)

item = driver.find_element_by_css_selector("a[class='wf-offer-link v-line-clamp ']");
item.click()
time.sleep(2)
driver.implicitly_wait(15)

review = driver.find_element_by_css_selector("span[class='popover-wrapper']");
review.click()
time.sleep(2)
driver.implicitly_wait(15)

pageSource = driver.page_source
fileToWrite = open("bestbuy_deal_of_the_day.htm", "w")
fileToWrite.write(pageSource)
fileToWrite.close()
fileToRead = open("bestbuy_deal_of_the_day.htm", "r")
fileToRead.close()
time.sleep(2)


driver.quit()

print(f"The time left for the deal: {Hour}:{Min}:{Sec}")

with open('DDR_HW4.txt', 'w') as f:
    print('The time left for the deal:',Hour,':',Min,':',Sec, file=f)
f.close()
    


# In[ ]:




