# -*- coding: utf-8 -*-

from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import commons
# import selenium-chrome-screenshot

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        # self.browser = webdriver.Firefox()
        self.browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        self.browser.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        url = "http://52.38.165.143:3000/dashboard/db/4know?orgId=1"
        # picName = url.replace(".html", ".png")
        picName = "4KnowSys.png"
        # fireFoxOptions = webdriver.FirefoxOptions()
        ChromeOptions = webdriver.ChromeOptions()
        ChromeOptions.set_headless()
        #browser = webdriver.Firefox(firefox_options=fireFoxOptions)

        browser = self.browser
        browser.get(url)
        #browser.find_element_by_name("username").click()
        #browser.find_element_by_name("username").clear()
        browser.find_element_by_name("username").send_keys("admin")
        #browser.find_element_by_id("inputPassword").clear()
        browser.find_element_by_id("inputPassword").send_keys("admin")
        browser.find_element_by_name("loginForm").submit()
        browser.find_element_by_css_selector("button.btn.btn-large.p-x-3.btn-primary").click()

        time.sleep(15)

        browser.maximize_window()

        # selenium.captureEntirePageScreenshot("C:\www\1.png", "")
        time.sleep(5)
        browser.save_screenshot(picName)
        #browser.close()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.browser.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.browser.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

 #   def tearDown(self):
 #       self.browser.quit()
 #       self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

