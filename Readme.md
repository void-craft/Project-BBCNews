### Project-BBCNews

* This is a framework written to test BBC Websites features. 

* It is written using Selenium/Python, with BDD implementation using Behave in Gherkin language.

* It has Page Object Model implementation.

* Logging featured is included to document the tests.

* Environment is set up for before and after scenario to reduce duplication of code. 

## The following features are tested:

### 1. News: Different sections of news are clicked in the below scenarios, to validate each one.

   a. World
   b. Science
   c. Tech
   d. Climate
   e. Business

### 2. Video: Playback functionality of video on the website is checked 

   a. Play 
   b. Pause

## Commands to run the tests:

### 1. To run the features:

   a. behave features\news.feature
   b. behave features\video.feature

### 2. The results can be generated using allure-behave:

   a. behave -f allure_behave.formatter:AllureFormatter -o reports/ ./features/news.feature
   b. behave -f allure_behave.formatter:AllureFormatter -o reports/ ./features/video.feature

### 3. The results are converted to html files for readability using:

   allure serve reports/
