import pytest
from pageobjects.homepage import Homepage
from utilities.custom_logger import LogGen
from selenium import webdriver


class Test001HomepageLoading:
    LOGGER = LogGen.log_gen()

    @pytest.mark.regression
    def test_cookie_rejection(self, setup):
        self.LOGGER.info("************* Test001CookieRejection **********")
        self.driver = webdriver.Chrome()
        self.driver = setup

        self.driver.get("https://www.bbc.com")
        self.homepage = Homepage(self.driver)
        self.LOGGER.info("************* Cookie Rejection Test Started **********")
        self.homepage.reject_cookies(Homepage.FRAME_IFRAME_ID, Homepage.BUTTON_REJECT_COOKIES_XPATH)

        if self.driver.find_element(self.homepage.LINK_HOMEPAGE_XPATH):
            self.driver.close()
            self.LOGGER.info("************* Cookie Rejection Test Passed **********")
            assert True
        else:
            self.driver.close()
            self.LOGGER.error("************* Cookie Rejection Test Failed **********")
            assert False

    @pytest.mark.regression
    def test_homepage_loading(self, setup):
        self.LOGGER.info("******* Test002HomepageLoading **********")
        self.driver = setup
        self.LOGGER.info("************* Homepage Loading Test Started **********")
        self.driver.get("https://www.bbc.com")
        self.homepage = Homepage(self.driver)
        self.homepage.reject_cookies(Homepage.FRAME_IFRAME_ID, Homepage.BUTTON_REJECT_COOKIES_XPATH)

        homepage_links = self.driver.find_elements(*Homepage.LINK_HOMEPAGE_XPATH)
        if not homepage_links:
            self.driver.close()
            self.LOGGER.error("************* Homepage Loading Test Failed **********")
            assert False
        else:
            self.driver.close()
            self.LOGGER.info("************* Homepage Loading Test Passed **********")
            assert True
