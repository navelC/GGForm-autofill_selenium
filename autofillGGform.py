# Import Module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from threading import Thread
import threading
import time
import random

def fill10GGForm():

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    # open Chrome
    driver = webdriver.Chrome(
        'C:/Users/boong/.webdrivers/chromedriver.exe',chrome_options=options)
    driver.maximize_window()
    # Open URL
    driver.get('https://docs.google.com/forms/u/1/d/e/1FAIpQLSdGoflRSWdvE0fgsc9xnn0VSaHhT2LKMtOIcnvDBZQl180gcg/viewform')

    # wait for one second, until page gets fully loaded


    # Data

    for x in range(10):
        time.sleep(1)
        #form 1
        q1 = driver.find_elements(by=By.CLASS_NAME, value="AB7Lab")
        q1[0].click()   

        next = driver.find_element(by=By.XPATH, value=
            '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')
        next.click()

        #form 2
        time.sleep(1)
        q2 = driver.find_elements(by=By.CLASS_NAME, value= 
            'uHMk6b') 
        q2[random.randint(1, 2)].click()   
        q3 = driver.find_elements(by=By.CLASS_NAME, value= 
            "AB7Lab")
        count = 0 
        ran = random.randint(0, 3)
        for x in q3:
            if count == ran: 
                x.click()  
            count = count+1
            if count == 4:
                count = 0
                ran = random.randint(0, 3)
            

        next = driver.find_elements(by=By.XPATH, value=
            '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')[1].click()
        #form 3 

        q4 = driver.find_elements(by=By.CLASS_NAME, value= 
            'AB7Lab')
        count = 0 
        count0 =0
        lim = 0
        ran = random.randint(0, 4)
        #400
        for x in q4:
            # if count0 != lim:
            #     continue
            count0 = count0 + 1
            if count == ran: 
                try:
                    x.click()
                except:
                    pass
            count = count+1
            if count == 5:
                count = 0
                # count0 = count0 + 1 
                ran = random.randint(0, 4)

          

        next = driver.find_elements(by=By.XPATH, value=
            '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')[1].click()

        #form 4
        q5 = driver.find_elements(by=By.CLASS_NAME, value= 
            'AB7Lab')

        # q5[0-1] 1.
        # q5[2-4] 2. age
        # q5[5-9] 3. edu
        # q5[10-12] 4.
        # q5[13-17] 5.
        # q5[18-19] 6.
        age = random.randint(2, 4)
        min = 5 if age == 4 else 7
        max = 9 if age == 2 else 8
        edu = random.randint(min, max)

        q5[random.randint(0, 1)].click()
        q5[age].click()
        q5[edu].click()
        q5[12].click()
        q5[13].click()
        q5[18].click()   
        submit = driver.find_elements(by=By.XPATH, value=
            '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')[1].click()
            # fill another response
        another_response = driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        another_response.click()

for x in range(15):
    threading.Thread(target=fill10GGForm, args=()).start()
# close the window
