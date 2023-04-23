Feature: Browse BBC News sections
  As a user, I want to browse the BBC news website to see different news sections.

  Background:
    Given The user is on BBC News page
    When The user rejects the cookies
    Then The user should see the BBC News page loaded

  Scenario Outline: Browse BBC to reach a news section
    When The user clicks the <news_section> link
    Then The user should see the <news_section> news page loaded

    Examples:
      | news_section |
      | World        |
      | Climate      |
      | Business     |
      | Tech         |
      | Science      |
