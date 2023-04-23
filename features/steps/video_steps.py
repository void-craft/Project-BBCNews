from behave import given, when, then
import time


@given("The user is on the Video News page")
def step_impl(context):
    context.logger.info("***** Feature Scenario Test006BBCVideoNews Has Started *****")
    context.video_page.load()
    time.sleep(5)


@then('The user should see the Video page loaded')
def validate_video_page(context):
    title = context.video_page.validate_page()
    if "One-minute World News" in title:
        context.logger.info("Loaded Video News page successfully")
        assert True
    else:
        context.logger.error("Failed to load Video News page")
        assert False


@when("The user clicks the play button")
def step_impl(context):
    context.video_page.click_play_button()
    context.logger.info("Clicked on play button")


@then("The user sees the video start playing")
def step_impl(context):
    status = context.video_page.is_video_playing()
    if status:
        context.logger.info("Video is playing")
        assert True
    else:
        context.logger.error("Video failed to start playing")
        assert False


@when("The user clicks the pause button")
def step_impl(context):
    context.video_page.click_pause_button()
    context.logger.info("Clicked on pause button")


@then("The user should see the video pause")
def step_impl(context):
    status = context.video_page.is_video_paused()
    if status:
        context.logger.info("Video is paused")
        assert True
    else:
        context.logger.error("Video failed to pause")
        assert False
    context.logger.info("***** Feature Scenario Test006BBCVideoNews Has Ended *****")
