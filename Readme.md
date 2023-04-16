### Project_1

#### BBC_Webscraping - POM

This script is written Python Gherkin languages, that uses Selenium Framework. It has:

1. Page Object Model implementation with PyTest that automates opening a browser, navigating to the BBC website,
   rejecting cookies, clicking on various links to go to India news section, and printing the news headlines from the
   page, as well as
   using assert to check if the correct pages are loaded.

2. Behavior Driven Development with Behave module that uses background to launch the browser, reject cookies, click and
   validate several news sections.

   a. The results are generated using allure-behave:
   behave -f allure_behave.formatter:AllureFormatter -o Project_1/features/reports ./Project_1/features/

   b. Then they are converted to html files with the command:
   allure serve Project_1/features/reports
