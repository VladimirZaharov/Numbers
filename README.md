# Numbers
Запуск:
  1. Сделать копию файла .env.template > .env
  2. В файле .env: SECRET_KEY - секретный ключ Django
                SPREAD_SHEET_ID - id таблицы Google
                DATABASE=postgre
                DEBUG=False
                API_KEY - ключ api в google 
                TELEGRAM_TOKEN - токен бота в телеграмме
  3. создать базу в postgresql - numbers
  4. python manage.py migrate
  5. python run.py

Запуска докера не тестировался, не было возможности. В случае запуска с докером:
  1. Сделать копию файла .env.template > .env
  2. В файле .env: SECRET_KEY - секретный ключ Django, ввести любую комбинацию 
                   SPREAD_SHEET_ID - id таблицы Google
                   DATABASE=postgre
                   DEBUG=False
                   API_KEY - ключ api в google 
                   TELEGRAM_TOKEN - токен бота в телеграмме
  3. docker-compose up --build   

GET 127.0.0.1:8000/api/orders - Получение списка заказов 
GET 127.0.0.1:8000/api/orders/№ - Получение заказа, где № - номер заказа
