from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage


class Homepage(BasePage):
    BASE_URL = "https://www.bbc.com"
    LINK_HOMEPAGE_XPATH = By.XPATH, "//a[@id='homepage-link']"
    BUTTON_REJECT_COOKIES_XPATH = By.XPATH, "//button[contains(@title, 'I do not agree')]"
    LINK_NEWS_XPATH = By.XPATH, "(//a[.='News'])[2]"
    FRAME_IFRAME_ID = By.ID, "sp_message_iframe_783538"

    def load(self):
        self.driver.get(self.BASE_URL)

    def reject_cookies(self, frame_id, button_id):
        self.switch_to_frame(frame_id)
        self.click_element(button_id)
        self.switch_to_default_content()

    def click_news_link(self, locator):
        self.click_element(locator)

    def validate_page(self):
        title = self.get_title()
        return title
