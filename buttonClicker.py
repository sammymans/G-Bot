from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://shop.westernmustangs.ca/Program/GetProgramDetails?courseId=b48c8d0b-4493-4d3c-a4ed-9507063a9062&semesterId=81dac0e7-2456-44c9-bfe4-6ed494cc6824")

