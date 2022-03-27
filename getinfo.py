# Selenium
# Google Chrome Web Driver
from selenium import webdriver

PATH = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://www.thinkhalcyon.com")

print(driver.title)

# driver.quit() # Will quit the browser popup