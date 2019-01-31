Feature: Test navigation between pages



  Scenario: Home can go to Login
    Given I am on the homepage
    When I click on the dropdown menu
    Given I wait for the dropdown to load
    When I click on the "Log In" dropdown link
    Then I am on the login page

  Scenario: Home can go to Logout
    Given I am on the homepage
    When I click on the dropdown menu
    Given I wait for the dropdown to load
    When I click on the "Log Out" dropdown link
    Then I am on the login page

  Scenario: Home can go to Register
    Given I am on the homepage
    When I click on the dropdown menu
    Given I wait for the dropdown to load
    When I click on the "Sign In" dropdown link
    Then I am on the register page

  Scenario: Home can go to Digit Recognition
    Given I am on the homepage
    Given I wait for the page to load
    When I click the digit recognition link
    Then I am on the digit recognition page

  Scenario: Home can go to Classify Image
    Given I am on the homepage
    Given I wait for the page to load
    When I click the classify image link
    Then I am on the classify image page

  Scenario: Home can go to Cat Dog Classifier
    Given I am on the homepage
    Given I wait for the page to load
    When I click the cat dog classifier link
    Then I am on the cat dog classifier page