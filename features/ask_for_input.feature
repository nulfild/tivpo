Feature: запрос слова или буквы у игрока
  Scenario: игрок вводит слово или букву, подходящую условию и неиспользованную до этого
    Given слово или буква, введенная игроком
    When слово или буква, подходящая условию и неиспользованная до этого
    Then вернуть слово или букву в нижнем регистре

  Scenario: игрок вводит букву, подходящую условию, но использованную до этого
    Given буква, введенная игроком
    When буква, подходящая условию, но нспользованная до этого
    Then повторный запрос слова или буквы у игрока

  Scenario: игрок вводит слово или букву, которая не подохдит под условие
    Given слово или буква, введенная игроком
    When слово или буква не подходит условию
    Then повторный запрос слова или буквы у игрока