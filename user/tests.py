from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LoginTest(LiveServerTestCase):
	def setUp(self):
		self.selenium = webdriver.Firefox()
		super(LoginTest,self).setUp()

	def tearDown(self):
		self.selenium.quit()
		super(LoginTest,self).tearDown()

	def test_login(self):
		selenium = self.selenium
		selenium.get("http://127.0.0.1:8000")
		selenium.find_element(By.className("btn-gradient")).click()


