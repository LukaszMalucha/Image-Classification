Feature: Test that forms work correctly


  Scenario: Signup page registers user
    Given I am on the register page
    When I enter "tester1" in the "username" field
    And I enter "tester1@gmail.com" in the "email" field
    And I enter "12341234" in the "password" field
    And I press the submit button
    Then I am on the login page


  Scenario: Login page login user
    Given I am on the login page
    When I enter "tester" in the "username" login field
    And I enter "12341234" in the "password" login field
    And I press the submit button
    Then I am on the homepage


  Scenario: Digit Identifier page allows image download
    Given I am on the digit recognition page
    Given I wait for 3 sec
    When I press the download button
    Given I wait for the download image to finish
    Then I downloaded the image

  Scenario: Digit Recognition page allows digit prediction
    Given I am on the digit recognition page
    Given I wait for 3 sec
    When I press the predict button
    Then I can see there is the a prediction result on the page







