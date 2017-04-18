Feature: Checking the allegro page

  Scenario: Search for telefon
    Given the page "http://allegro.pl/" is loaded
    When I type "telefon" in "main-search-text" input
    And I click button with value "Szukaj"
    Then the result page is displayed with "Telefony i Akcesoria"

  Scenario: Search for telewizor
    Given the page "http://allegro.pl/" is loaded
    When I type "telewizor" in "main-search-text" input
    And I click button with value "Szukaj"
    Then the result page is displayed with "RTV i AGD"

  Scenario: Selecting podkategorie on the result page
    Given the page "https://allegro.pl/listing?string=telewizor&order=m&bmatch=s0-ele-1-4-0403" is loaded
    When I click on podkategoria "RTV i AGD"
    And I click on podkategoria "Piloty"
    Then the result page is displayed with "Uniwersalne"

  Scenario: Changing the location of products on z lubuskiego
    Given the page "https://allegro.pl/piloty-63489?string=telewizor&order=m&bmatch=s0-ele-1-4-0403" is loaded
    When I select "z lubuskiego" from wojewodztwo dropdown
    Then delete location option is available

@slow
  Scenario: Changing the location of products on z wielkopolskiego
    Given the page "https://allegro.pl/piloty-63489?string=telewizor&order=m&bmatch=s0-ele-1-4-0403" is loaded
    When I select "z wielkopolskiego" from wojewodztwo dropdown
    Then delete location option is available
