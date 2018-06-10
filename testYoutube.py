from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import *
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
        self.driver.find_element_by_xpath(XPATH_SORT_BY_VIEW_COUNT_BUTTON).click()
        time.sleep(2)
        # Store first value before loop
        prev_count = extract_view_count(self.driver.find_element_by_xpath(XPATH_VIDEO_VIEW_COUNT).text)
        # Iterate over view counts
        for count in self.driver.find_elements_by_xpath(XPATH_VIDEO_VIEW_COUNT):
            curr_count = extract_view_count(count.text)
            assert curr_count <= prev_count
            prev_count = curr_count

    def test_sort_by_upload_date(self):
        """ Test sort by upload date feature """
        self.driver.find_element_by_xpath(XPATH_SORT_BY_UPLOAD_DATE_BUTTON).click()
        time.sleep(WAIT_TIME)
        # Store first value before loop
        prev_upload_time = extract_upload_time(self.driver.find_element_by_xpath(XPATH_VIDEO_UPLOAD_TIME).text)
        # Iterate over view counts
        for dates in self.driver.find_elements_by_xpath(XPATH_VIDEO_UPLOAD_TIME):
            curr_upload_time = extract_upload_time(dates.text)
            assert curr_upload_time <= prev_upload_time
            prev_upload_time = curr_upload_time

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
