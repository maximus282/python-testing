# PODSTAWOWY PRZYKŁAD - kalkulator
# Feature = cała funkcjonalność aplikacji
Feature: Calculator operations
  As a user
  I want to perform basic math operations
  So that I can calculate results

  # Scenario = jeden konkretny test case
  Scenario: Adding two numbers
    Given I have a calculator
    When I add 2 and 3
    Then the result should be 5

  Scenario: Subtracting numbers
    Given I have a calculator
    When I subtract 5 from 10
    Then the result should be 5

  # Scenario Outline = parametryzowane testy (jak pytest.mark.parametrize)
  Scenario Outline: Multiple operations
    Given I have a calculator
    When I perform "<operation>" with <num1> and <num2>
    Then the result should be <expected>
    
    Examples:
      | operation | num1 | num2 | expected |
      | add       | 2    | 3    | 5        |
      | multiply  | 4    | 5    | 20       |
      | divide    | 10   | 2    | 5        |

  # Background = setup wspólny dla wszystkich scenariuszy (jak fixture)
  Scenario: Division by zero handling
    Given I have a calculator
    When I divide 10 by 0
    Then I should get an error message "Cannot divide by zero"