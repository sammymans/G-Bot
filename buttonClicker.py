from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://twitter.com/?lang=en")

driver.find_element_by_class_name("css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0").click()
