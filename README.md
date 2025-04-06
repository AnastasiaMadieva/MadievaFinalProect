# MadievaFinalProect

# pytest_ui_api_template

## Шаблон для автоматизации тестирования на python

### Шаги
1. Склонировать проект 'https://github.com/AnastasiaMadieva/MadievaFinalProect.git'
2. Установить зависимости 'pip3 freeze > requirements.txt'
3. Запустить тесты 'pytest -v -s'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

### Стек:
- pytest
- selenium
- requests
- _sqlalchemy_
- allure
- config

### Струткура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- ./db - хелперы для работы с БД

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)