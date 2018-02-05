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

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        url = "http://52.38.165.143:3000/dashboard/db/4know?orgId=1"
        # picName = url.replace(".html", ".png")
        picName = "4KnowSys.png"
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.set_headless()
        browser = webdriver.Firefox(firefox_options=fireFoxOptions)

        # dir_name = "screenshot" #这里定义了截图存放目录名
        # if (!(new File(dir_name).isDirectory())) {# 判断是否存在该目录
        # new File(dir_name).mkdir(); # 如果不存在则新建一个目录
        # }
        #
        # SimpleDateFormat
        # sdf = new
        # SimpleDateFormat("yyyyMMdd-HHmmss");
        # String
        # time = sdf.format(new
        # Date()); # 这里格式化当前时间，例如20120406 - 165210，后面用的着
        #
        # try {
        # File source_file = ((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE); # 关键代码，执行屏幕截图，默认会把截图保存到temp目录
        # FileUtils.copyFile(source_file, new File(dir_name + File.separator + time + ".png")); # 这里将截图另存到我们需要保存的目录，例如screenshot\20120406-165210.png
        # } catch (IOException e) {
        # e.printStackTrace();
        # }

        # browser = self.browser
        browser.get(url)
        #browser.find_element_by_name("username").click()
        #browser.find_element_by_name("username").clear()
        browser.find_element_by_name("username").send_keys("admin")
        #browser.find_element_by_id("inputPassword").clear()
        browser.find_element_by_id("inputPassword").send_keys("admin")
        browser.find_element_by_name("loginForm").submit()
        browser.find_element_by_css_selector("button.btn.btn-large.p-x-3.btn-primary").click()

        time.sleep(15)

        #browser.maximize_window()

        # browser.execute_script("""
        #         (function () {
        #             var y = 0;
        #             var step = 100;
        #             window.scroll(0, 0);
        #
        #             function f() {
        #                 if (y < document.body.scrollHeight) {
        #                     y += step;
        #                     window.scroll(0, y);
        #                     setTimeout(f, 100);
        #                 } else {
        #                     window.scroll(0, 0);
        #                     document.title += "scroll-done";
        #                 }
        #             }
        #
        #             setTimeout(f, 1000);
        #         })();
        #     """)
        #
        # for i in xrange(30):
        #     if "scroll-done" in browser.title:
        #         break
        #     time.sleep(1)

        # selenium.captureEntirePageScreenshot("C:\www\1.png", "")
        browser.set_window_size(1920,1920)
        time.sleep(1)
        browser.get_screenshot_as_file("1920.png")
        browser.set_window_size(1920,1024)
        browser.get_screenshot_as_file("1024.png")
        browser.maximize_window()
        browser.get_screenshot_as_file("test.png")
        browser.fullscreen_window()
        browser.get_screenshot_as_file("full.png")
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

