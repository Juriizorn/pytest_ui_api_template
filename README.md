# pytest_ui_api_template

## Шаблон для автоматизации тестирования на Python

### Шаги

1. Клонировать проект себе на компьютер 'git clone https://github.com/Juriizorn/pytest_ui_api_template.git'
2. Установить все зависимости
3. Запустить тесты 'pytest'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

### Стек

- pytest
- selenium
- request
- sqlalchemy
- allure
- config

### Структура

- ./test
- ./pages
- ./api
- ./db
- ./configuration - провайдер настроек
- - test_config.ini - настройки для тестов
- ./test_data - провайдер тестовых данных
- - test_data.json

### Полезные ссылки

- [Подсказка по Markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)

### Библиотеки

- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest