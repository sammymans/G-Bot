from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://shop.westernmustangs.ca/Program/GetProgramDetails?courseId=b48c8d0b-4493-4d3c-a4ed-9507063a9062&semesterId=81dac0e7-2456-44c9-bfe4-6ed494cc6824")

link = driver.find_element_by_link_text("REGISTER")
link.click()

try: 
    element= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button.loginOption btn btn-lg btn-block btn-social btn-linkedin")))
    element.click()
except:
    driver.quit()





