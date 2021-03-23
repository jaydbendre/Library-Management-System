from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxOptions
import os

class LoginTest(LiveServerTestCase):
	def setUp(self):
		opts = FirefoxOptions()
		opts.add_argument("--headless")	
		self.selenium = webdriver.Firefox(service_log_path = "./geckodriver.log",options=opts)
		super(LoginTest,self).setUp()

	def tearDown(self):
		self.selenium.quit()
		super(LoginTest,self).tearDown()

	def test_login(self):
		selenium = self.selenium
		selenium.get("http://localhost:8000")
		selenium.find_element_by_class_name("btn-gradient").click()


