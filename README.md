# Numbers
Запуск:
  1. Сделать копию файла .env.template > .env
  2. В файле .env: SECRET_KEY - секретный ключ Django
                SPREAD_SHEET_ID - id таблицы Google
                DATABASE=postgre
                DEBUG=False
                API_KEY - ключ api в google 
                TELEGRAM_TOKEN - токен бота в телеграмме
  3. python manage.py migrate
  4. python run.py

Запуска докера не тестировался, не было возможности. В случае запуска с докером:
  1. Сделать копию файла .env.template > .env
  2. В файле .env: SECRET_KEY - секретный ключ Django
                SPREAD_SHEET_ID - id таблицы Google
                DATABASE=postgre
                DEBUG=False
                API_KEY - ключ api в google 
                TELEGRAM_TOKEN - токен бота в телеграмме
  3. docker-compose up --build   