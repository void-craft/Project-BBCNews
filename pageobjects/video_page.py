import time
from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage


class VideoPage(BasePage):
    VIDEO_URL = "https://www.bbc.com/news/av/10462520"
    IFRAME_VIDEO_PLAYER_ID = By.ID, "smphtml5iframebbcMediaPlayer0"
    MEDIA_CONTAINER_ID = By.ID, "mediaContainer"
    BUTTON_PLAY_XPATH = By.XPATH, "//button[@class='p_button p_controlBarButton p_playButton']"
    BUTTON_PAUSE_XPATH = By.XPATH, "//button[@class='p_button p_controlBarButton p_pauseButton']"
    CONTROL_BAR_XPATH = By.XPATH, "//div[@class='p_playerControlBarHolder']"

    def load(self):
        self.driver.get(self.VIDEO_URL)

    def click_play_button(self):
        time.sleep(5)
        self.switch_to_frame(self.IFRAME_VIDEO_PLAYER_ID)
        self.click_element(self.MEDIA_CONTAINER_ID)
        time.sleep(5)

    def is_video_playing(self):
        self.press_arrow_down()
        self.hover_over_element(self.CONTROL_BAR_XPATH)
        if self.wait_for_element(self.BUTTON_PAUSE_XPATH):
            return True
        else:
            return False

    def click_pause_button(self):
        self.click_element(self.BUTTON_PAUSE_XPATH)

    def is_video_paused(self):
        self.scroll_to_element(self.CONTROL_BAR_XPATH)
        if self.wait_for_element(self.BUTTON_PLAY_XPATH):
            return True
        else:
            return False

    def validate_page(self):
        title = self.get_title()
        return title
