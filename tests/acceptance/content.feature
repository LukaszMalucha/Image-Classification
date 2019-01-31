Feature: Test that page have correct content

  Scenario: Homepage has a correct title
    Given I am on the homepage
    Given I wait for 3 sec
    Then There is a title shown on the page
    And The title tag has content "Image Recognition"

  Scenario: Signup page loads the form
   Given I am on the register page
   Then I can see there is a register form on the page

  Scenario: Login page loads the form
   Given I am on the login page
   Then I can see there is a login form on the page

  Scenario: Digit recognition page has all three buttons
    Given I am on the digit recognition page
    Then There are three buttons shown on the page


