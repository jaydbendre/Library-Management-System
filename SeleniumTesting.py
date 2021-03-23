import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import FireFoxOptions

import time

opts = FireFoxOptions()
opts.add_argument("--headless")

browser = webdriver.Firefox(executable_path = "./drivers/geckodriver",service_log_path = "./geckodriver.log",options = opt)
browser.get("http://localhost:8000")

browser.find_element(By.className("btn-gradient")).click()

time.sleep(5)
browser.quit()
