from selenium import webdriver
from pageobjects.homepage import Homepage
from pageobjects.news_page import NewsPage
from pageobjects.video_page import VideoPage
from utilities.custom_logger import LogGen


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    context.driver = webdriver.Chrome(options=options)
    context.driver.maximize_window()
    context.homepage = Homepage(context.driver)
    context.news_page = NewsPage(context.driver)
    context.video_page = VideoPage(context.driver)
    context.logger = LogGen.log_gen()


def after_scenario(context, scenario):
    context.driver.delete_all_cookies()
    context.driver.quit()
