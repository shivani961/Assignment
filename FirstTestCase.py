
import time
from sys import executable
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo") #Launching the website
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("New York")

time.sleep(10)
rows = driver.find_elements(By.XPATH,"//table[@id='example']//tr")
if(len(rows)) == 6:
    print("Showing Correct Result")
else:
    print("Showing Incorrect Result")
