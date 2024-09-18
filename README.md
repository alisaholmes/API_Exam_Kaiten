# Дипломный проект по тестированию API-запросов сайта таск-трекера "Kaiten"

### [Ссылка на сайт](https://kaiten.ru/)

## Содержание
- [Технологии и инструменты](#технологии-и-инструменты)
- [Список проверок, реализованных в автотестах](#список-проверок-реализованных-в-автотестах)
- [Сборка проекта и запуск тестов в Jenkins с параметрами](#сборка-проекта-и-запуск-тестов-в-jenkins-с-параметрами)
- [Отчет о результатах тестирования в Allure-reports](#отчет-о-результатах-тестирования-в-allure-reports-)
- [Автоматическое оповещение о результатах сборки Jenkins в Telegram-бот](#автоматическое-оповещение-о-результатах-сборки-jenkins-в-telegram-бот)
- [Дашборд Allure TestOps](#дашборд-allure-testops)


## Технологии и инструменты
Проект реализован с использованием Python, PyCharm, Pytest, Allure Report, Jenkins, Allure TestOps, Telegram, Jira.
<p align="left">

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height="40" width="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg" height="40" width="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg" height="40" width="40"/>
<img src="https://camo.githubusercontent.com/e8c35be9136635c1b2e2b22b112e02ef1fb9e9434970df18d84071a2e714d3e0/68747470733a2f2f616c6c7572657265706f72742e6f72672f7075626c69632f696d672f616c6c7572652d7265706f72742e737667" title="allure" alt="allure" width="40" height="40"/>&nbsp     
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height="40" width="40"/>      
<img src="design/icons/allure_testops.svg" height="40" width="40"/>     
<img src="design/icons/telegram.png" height="40" width="40"/>     
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jira/jira-original.svg" height="40" width="40"/> 

## Список проверок API, реализованных в автотестах

- [x] Проверка успешной авторизации (GET-запрос)
- [x] Проверка успешного получения списка пространств (GET-запрос)
- [x] Проверка успешного получения одного пространства (GET-запрос)
- [x] Проверка успешного создания нового пространства (POST-запрос)
- [x] Проверка успешного создания новой доски (POST-запрос)
- [x] Проверка успешного удаления пространства (DELETE-запрос)
 

## <img src="https://camo.githubusercontent.com/e8c35be9136635c1b2e2b22b112e02ef1fb9e9434970df18d84071a2e714d3e0/68747470733a2f2f616c6c7572657265706f72742e6f72672f7075626c69632f696d672f616c6c7572652d7265706f72742e737667" title="allure" alt="allure" width="30" height="30"/> Отчет в Allure report</a></a>

<details><summary>Основной отчет</summary>

<img src="design/images/allure.png">

</details>
<details><summary>Тесты</summary>

<img src="design/images/allure_logs.png">

</details>