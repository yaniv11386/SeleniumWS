from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from params import *
from datetime import datetime
import unittest
import time


class TestYoutubeFilter(unittest.TestCase):
    def setUp(self):
        """ Open Youtube, search video and click 'Filter' button """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.youtube.com")
        self.driver.find_element_by_xpath(XPATH_SEARCH_FIELD).send_keys(SEARCH_TERM)
        self.driver.find_element_by_xpath(XPATH_SEARCH_BUTTON).click()
        WebDriverWait(self.driver, WAIT_TIME).until(EC.title_contains(SEARCH_TERM))
        time.sleep(WAIT_TIME)
        self.driver.find_element_by_xpath(XPATH_FILTER_BUTTON).click()

    def test_sort_by_view_count(self):
        """ Test sort by view count feature """
        pass

    # def test_sort_by_upload_date(self):
    #     """ Test sort by upload date feature """
    #     pass
    #
    # def test_filter_short_duration(self):
    #     """ Test filter short videos (< 4 minutes) feature """
    #     pass
    #
    # def test_filter_long_duration(self):
    #     """ Test filter long videos (> 20 minutes) feature """
    #     pass

    def tearDown(self):
        """ Close webdriver"""
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
