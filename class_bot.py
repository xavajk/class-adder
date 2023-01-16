import time
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pandas as pd

service = Service('/Users/xava/Documents/Projects/selenium/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)

def login(username, password):
    # open the webpage
    driver.get('https://ecampus.scu.edu/psp/csprd92/?cmd=login&languageCd=ENG&')

    # get sign in elements
    id = driver.find_element(By.ID, 'userid')
    pwd = driver.find_element(By.ID, 'pwd')
    submit = driver.find_element(By.NAME,'Submit')

    # enter fields
    id.send_keys(username)
    pwd.send_keys(password)
    submit.click()
    # time.sleep(3)

def pick_quarter():
    # navigate to manage classes page
    classes = driver.find_element(By.ID, 'win0divPTNUI_LAND_REC_GROUPLET$1')
    classes.click()
    # time.sleep(3)

    # close sidebar
    tab = driver.find_element(By.ID, 'PT_SIDE$PIMG')
    tab.click()
    time.sleep(3)

    # switch to correct frame
    frame = driver.find_element(By.ID, 'main_target_win0')
    driver.switch_to.frame(frame)

    # get quarter out of table
    table = driver.find_element(By.CSS_SELECTOR, '#SSR_DUMMY_RECV1\$scroll\$0 > tbody > tr:nth-child(2) > td > table')
    rows = table.find_elements(By.TAG_NAME, 'tr')

    quarter = rows[len(rows) - 1].find_element(By.TAG_NAME, 'input')
    quarter.click()
    time.sleep(1)
    
    submit = driver.find_element(By.ID, 'DERIVED_SSS_SCT_SSR_PB_GO')
    submit.click()
    time.sleep(5)

    print('her')
    # click on the quarter

def add_class(class_number):
    # enter class number
    class_num = driver.find_element(By.ID, 'DERIVED_REGFRM1_CLASS_NBR')
    class_num.send_keys(class_number)
    time.sleep(1)

    # click on the add class button
    enter = driver.find_element(By.ID, 'DERIVED_REGFRM1_SSR_PB_ADDTOLIST2$9$')
    enter.click()
    time.sleep(3)

    next = driver.find_element(By.ID, 'DERIVED_CLS_DTL_NEXT_PB$280$')
    next.click()
    time.sleep(3)
    
    print('Adding a class')

def add_classes(file):
    # switch to correct frame
    frame = driver.find_element(By.ID, 'ptifrmtgtframe')
    driver.switch_to.frame(frame)

    classes = pd.read_csv(file)
    for c in classes:
        add_class(c)
        time.sleep(5)

    proceed = driver.find_element(By.ID, 'DERIVED_REGFRM1_LINK_ADD_ENRL$82$')
    proceed.click()
    time.sleep(1)

    enroll = driver.find_element(By.ID, 'DERIVED_REGFRM1_SSR_PB_SUBMIT')
    enroll.click()
    time.sleep(1)