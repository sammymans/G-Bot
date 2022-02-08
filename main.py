#import imp
from msilib.schema import ServiceControl
import time
from tkinter import E
from webbrowser import Chrome

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from login import username, password, first, last, home, mobile, email, saved2

import options
from options import time_option

from pickSport import my_url, sport_picked

# Only import if Squash is selected
if sport_picked == 6:
    from pickSport import pemail, fname, student_id

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

PATH = "C:\Program Files (x86)\chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(PATH)
driver.get(my_url)
driver.maximize_window()

try:
    # Acknowledge cookies
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "gdpr-cookie-accept")))
    element.click()
    print("Cookies")

    # Click Register
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Register")))
    element.click()
    print("Initial Registered")

    # Click Western Login
    element = WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='section-sign-in-first']/div[6]/div/button")))
    element.click()
    print("Signed in")

    # Fill username
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "userId")))
    element.clear()
    element.send_keys(username)
    print("Username")

    # Fill password
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "password")))
    element.clear()
    element.send_keys(password)
    print("Password")

    # Click Submit
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='fm1']/fieldset/div[3]/input[4]")))
    element.click()
    print("Submit")

    # Click Proper Register Button
    elements = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "card-body")))
    element = elements[time_option].find_element(
        By.TAG_NAME, "button")
    element.click()
    print("Correct Register")

    if sport_picked in [8, 10]:
        if saved2 == 0:
            # Add Person
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "btAdd-pickup")))
            element.click()
            print("Add Person")

            # Fill first
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "firstName")))
            element.clear()
            element.send_keys(first)
            print("FirstName")

            # Fill last
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "lastName")))
            element.clear()
            element.send_keys(last)
            print("LastName")

            # Fill Home
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "primaryPhone")))
            element.clear()
            element.send_keys(home)
            print("Homephone")

            # Fill Mobile
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "secondaryPhone")))
            element.clear()
            element.send_keys(mobile)
            print("mobile phone")

            # Fill Email
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "emailAddress")))
            element.clear()
            element.send_keys(email)
            print("email")

            # Click Save
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='addPersonContact']/div[2]/button[2]")))
            element.click()
            print("Save Click")

        # Click Continue
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="mainContent"]/div[2]/div/a')))
        element.click()
        print("Continue")

    # Fill-in Textbox Options
    if sport_picked in [1, 2]:
        vaccinelocation = 5
    elif sport_picked in [4, 5]:
        vaccinelocation = 2
    elif sport_picked == 7:
        vaccinelocation = 1
    elif sport_picked == 6:
        vaccinelocation = 6
    elif sport_picked == 8:
        vaccinelocation = 3
    elif sport_picked == 9:
        vaccinelocation = 4
    else:
        vaccinelocation = 0
    print("Vaccine Location {}".format(vaccinelocation))

    # Click Yes For Loop
    elements = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "input#rbtnYes")))
    for i in range(len(elements)):
        if sport_picked in [4, 5]:  # To handle Vaccine Textbox being in the middle
            if i < vaccinelocation:
                element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                    (By.NAME, "CustomPrompts[{}].CommonInput".format(i))))
                element.click()
            else:
                element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                    (By.NAME, "CustomPrompts[{}].CommonInput".format(i+1))))
                element.click()
        elif sport_picked == 6:  # To handle Partner Info Textbox being in the middle
            if i < (vaccinelocation-2):
                element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                    (By.NAME, "CustomPrompts[{}].CommonInput".format(i))))
                element.click()
            else:
                element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                    (By.NAME, "CustomPrompts[{}].CommonInput".format(i+1))))
                element.click()
        else:
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.NAME, "CustomPrompts[{}].CommonInput".format(i))))
            element.click()
    print("Yes Clicked")

    # Typing Agree to Vaccine Textbox
    if sport_picked in [1, 2, 4, 5, 6, 7, 8, 9]:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.NAME, "CustomPrompts[{}].CommonInput".format(vaccinelocation))))
        element.clear()
        element.send_keys("Agree")
        print("Vaccine Agreed")
    print("Sport Picked{}".format(sport_picked))
    # Typing Partner Info for Squash
    if sport_picked == 6:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.NAME, "CustomPrompts[4].CommonInput")))
        element.clear()
        element.send_keys("{}, {}, {}".format(fname, pemail, student_id))
        print("Squash Partner Info")

    # Click Add to Cart
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="mainContent"]/div[2]/form[2]/div[2]/button[2]')))
    element.click()
    print("Add to Cart")

    # Click Checkout
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'checkoutButton')))
    element.click()

    # Click Checkout Again
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="CheckoutModal"]/div/div/div[2]/button[2]')))
    # UN-COMMENT THE LINE BELOW TO FOLLOW THROUGH WITH CHECKOUT AND CLAIM THE BOOKING SPOT
    # element.click()
    driver.implicitly_wait(2)
except:
    driver.quit()
