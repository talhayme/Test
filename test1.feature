Feature: Checking search
Scenario: Сheck some text in search results
#Шаги
  Given website «www.yandex.ru»
  Then push button with text 'Найти'
  Then page include text 'Задан пустой поисковый запрос'
