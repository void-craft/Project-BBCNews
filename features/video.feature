Feature: Verify video playback functionality

Scenario: Play and pause video
    Given The user is on the Video News page
    When The user rejects the cookies
    Then The user should see the Video page loaded
    When The user clicks the play button
    Then The user sees the video start playing
    When The user clicks the pause button
    Then The user should see the video pause
