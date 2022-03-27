# Selenium
# Google Chrome Web Driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://www.wikipedia.com")

print(driver.title)

# driver.quit() # Will quit the browser popup