from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage


class NewsPage(BasePage):
    URL_NEWS = "https://www.bbc.com/news"
    LINK_WORLD_XPATH = By.XPATH, "(//span[.='World'])[1]"
    LINK_CLIMATE_XPATH = By.XPATH, "(//span[.='Climate'])[1]"
    LINK_BUSINESS_XPATH = By.XPATH, "(//span[.='Business'])[1]"
    LINK_TECH_XPATH = By.XPATH, "(//span[.='Tech'])[1]"
    LINK_SCIENCE_XPATH = By.XPATH, "(//span[.='Science'])[1]"

    def load(self):
        self.driver.get(self.URL_NEWS)

    def click_a_link(self, locator):
        self.click_element(locator)

    def validate_page(self):
        title = self.get_title()
        return title
