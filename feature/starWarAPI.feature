# Created by SrikantaKumar at 7/22/2022
Feature: Verify the starWar API for people
  # Enter feature description here

  Scenario: Verify Get People API
    Given swapi API details with people are there
    When we execute GET people API
    Then It gives the list of all people 