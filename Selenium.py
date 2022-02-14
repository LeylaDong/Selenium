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




