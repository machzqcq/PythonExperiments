Feature: Call Jira APIs

  Scenario: Retrieve application properties
    When I query jira
    Then I list all issues for "pmacharl"