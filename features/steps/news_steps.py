from behave import given, when, then
from pageobjects.news_page import NewsPage
from pageobjects.homepage import Homepage


@given('The user is on BBC News page')
def go_to_bbc_news_page(context):
    context.logger.info("Navigating to the BBC News page")
    context.news_page.load()


@when('The user rejects the cookies')
def reject_cookies(context):
    context.logger.info("Rejecting cookies by clicking on the Reject Cookies button")
    context.homepage.reject_cookies(Homepage.FRAME_IFRAME_ID, Homepage.BUTTON_REJECT_COOKIES_XPATH)


@then('The user should see the BBC News page loaded')
def validate_news_page_loaded(context):
    context.logger.info("Validating that the BBC News page is loaded")
    title = context.news_page.validate_page()
    if "News" in title:
        context.logger.info("BBC News page loaded successfully")
        assert True
    else:
        context.logger.error("Failed to load the BBC News page")
        assert False


@when('The user clicks the world link')
def click_world_link(context):
    context.logger.info("***** Feature Scenario Test001World Has Started *****")
    context.logger.info("Clicking on the World link")
    context.news_page.click_a_link(NewsPage.LINK_WORLD_XPATH)


@then('The user should see the world news page loaded')
def validate_world_page_loaded(context):
    context.logger.info("Validating that the BBC World News page is loaded")
    title = context.news_page.validate_page()
    if "World" in title:
        context.logger.info("BBC World News page loaded successfully")
        assert True
    else:
        context.logger.error("Failed to load the BBC World News page")
        assert False
    context.logger.info("***** Feature Scenario Test001BBCWorldNews Has Ended *****")


@when('The user clicks the climate link')
def click_climate_link(context):
    context.logger.info("***** Feature Scenario Test002BBCClimateNews Has Started *****")
    context.logger.info("Clicking on the Climate link")
    context.news_page.click_a_link(NewsPage.LINK_CLIMATE_XPATH)


@then('The user should see the climate news page loaded')
def validate_climate_page_loaded(context):
    context.logger.info("Validating that the BBC Climate News page is loaded")
    title = context.news_page.validate_page()
    if "Climate" in title:
        context.logger.info("BBC Climate News page loaded successfully")
        assert True
    else:
        context.logger.error("Failed to load the BBC Climate News page")
        assert False
    context.logger.info("***** Feature Scenario Test002BBCClimateNews Has Ended *****")


@when('The user clicks the business link')
def click_business_link(context):
    context.logger.info("***** Feature Scenario Test003BBCBusinessNews Has Started *****")
    context.logger.info("Clicking on the Business link")
    context.news_page.click_a_link(NewsPage.LINK_BUSINESS_XPATH)


@then('The user should see the business news page loaded')
def validate_business_page_loaded(context):
    context.logger.info("Validating that the BBC Business News page is loaded")
    title = context.news_page.validate_page()
    if "Business" in title:
        context.logger.info("BBC Business News page loaded successfully")
        assert True
    else:
        context.logger.error("Failed to load the BBC Business News page")
        assert False
    context.logger.info("***** Feature Scenario Test003BBCBusinessNews Has Ended *****")


@when('The user clicks the tech link')
def click_tech_link(context):
    context.logger.info("***** Feature Scenario Test004BBCTechNews Has Started *****")
    context.logger.info("Clicking on the Tech link")
    context.news_page.click_a_link(NewsPage.LINK_TECH_XPATH)


@then('The user should see the tech news page loaded')
def validate_tech_page_loaded(context):
    context.logger.info("Validating that the BBC Tech News page is loaded")
    title = context.news_page.validate_page()
    if "Tech" in title:
        context.logger.info("BBC Tech News page loaded successfully")
        assert True
    else:
        context.logger.error("Failed to load the BBC Tech News page")
        assert False
    context.logger.info("***** Feature Scenario Test004BBCTechNews Has Ended *****")


@when('The user clicks the science link')
def click_science_link(context):
    context.logger.info("***** Feature Scenario Test005BBCScienceNews Has Started *****")
    context.logger.info("Clicking on the Science link")
    context.news_page.click_a_link(NewsPage.LINK_SCIENCE_XPATH)


@then('The user should see the science news page loaded')
def validate_science_page_loaded(context):
    context.logger.info("Validating that the BBC Science News page is loaded")
    title = context.news_page.validate_page()
    if "Science" in title:
        context.logger.info("BBC Science News page loaded successfully")
        assert True
    else:
        context.logger.error("Failed to load the BBC Science News page")
        assert False
    context.logger.info("***** Feature Scenario Test005BBCScienceNews Has Ended *****")
