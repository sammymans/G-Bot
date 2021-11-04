from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


from login import username, password

from login import first, last, home, mobile, email, saved2

import gBot
from gBot import time_Option

from picking_sport import my_url,sportpicked
if sportpicked ==7:
    from picking_sport import pemail, fname, student_id

    
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH,options=chrome_options)

driver.get(my_url)
try: 
    # Acknowledge cookies
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"gdpr-cookie-accept")))
    element.click()

    # Click Register
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"REGISTER")))
    element.click()
    
    # Click Western Login
    element= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='divLoginOptions']/div[2]/div[2]/div/button")))
    element.click()

    # Fill username
    element= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"userId")))
    element.clear()
    element.send_keys(username)
    
    # Fill password
    element= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"password")))
    element.clear()
    element.send_keys(password)

    # Click Submit
    element= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='fm1']/fieldset/div[3]/input[4]")))
    element.click()

    # Click Proper Register Button
    elements= WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"button.btn-primary")))
    elements[time_Option].click()


    if saved2==0:
        # Add Person
        element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"btAdd")))
        element.click()


        # Fill first
        element= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"firstName")))
        element.clear()
        element.send_keys(first)
    
        # Fill last
        element= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"lastName")))
        element.clear()
        element.send_keys(last)

        #Fill Home 
        element= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"primaryPhone")))
        element.clear()
        element.send_keys(home)

        #Fill Mobile
        element= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"secondaryPhone")))
        element.clear()
        element.send_keys(mobile)

        #Fill Email
        element= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"emailAddress")))
        element.clear()
        element.send_keys(email)

        #Click Save
        element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='addPersonContact']/div[2]/button[2]")))
        element.click()

    #Click Continue
    if sportpicked in [1,2,9]:
        element= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="mainContent"]/div[2]/div[2]/a')))
        element.click()

    #Click Yes For Loop
    elements= WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"input#rbtnYes")))
    for i in range(len(elements)):
        element= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"CustomPrompts["+str(i)+"].CommonInput")))
        element.click()
    
    
    if sportpicked == 2:   
        element= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"CustomPrompts[5].CommonInput")))
        element.click()
    elif sportpicked == 6:
        element= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"CustomPrompts[3].CommonInput")))
        element.click()


    if sportpicked==7:
        element= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"textarea.form-control")))
        element.clear()
        element.send_keys(fname+","+student_id+","+pemail)
        element= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"CustomPrompts[5].CommonInput")))
        element.click()
        element= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="CustomPrompts_6__CommonInput"]')))
        element.clear()
        element.send_keys("Yes")
        

    else:
        #Type Yes
        element= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"textarea.form-control")))
        element.clear()
        element.send_keys("Yes")



    #Click Add to Cart
    element= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="mainContent"]/div[2]/form[2]/div[2]/button[2]')))
    element.click()

    #Click Checkout
    element= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'checkoutButton')))
    element.click()

    #Click Checkout Again
    element= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="CheckoutModal"]/div/div[2]/button[2]')))
    #element.click()


except:
    driver.quit()
