from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login import username
from login import password


import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://shop.westernmustangs.ca/Program/GetProgramDetails?courseId=b48c8d0b-4493-4d3c-a4ed-9507063a9062&semesterId=81dac0e7-2456-44c9-bfe4-6ed494cc6824")

#link = driver.find_element_by_link_text("REGISTER")
#link.click()

try: 
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"REGISTER")))
    element.click()
    
    element= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='divLoginOptions']/div[2]/div[2]/div/button")))
    element.click()

    element= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"userId")))
    element.clear()
    element.send_keys(username)

    element= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"password")))
    element.clear()
    element.send_keys(password)

    element= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='fm1']/fieldset/div[3]/input[4]")))
    element.click()

except:
    driver.quit()

