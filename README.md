# Messenger

## Запуск

Для установки всех зависимостей выполнить `pip install -r requirements.txt`

Создать суперпользователя командой `python manage.py createsuperuser`

Для запуска выполнить `python manage.py runserver`

Запустить Kafka на порту `9092`, и в ней создать топик с именем `Messages`

Для запуска Листенера в папке api_service запустить файл `consumer.py`

## Использование

Для получения JWT-токена перейти по ссылке `http://127.0.0.1:8000/api/v1/token`, и вставить имя и пароль суперпользователя, после чего скопировать access токен

Для добавления сообщения перейти по ссылке `http://127.0.0.1:8000/api/v1/message`, в поле Token вставить access токен, если указать недействительный токен, то сообщение не будет проверяться Листенером

Для получения списка сообщений перейти по ссылке `http://127.0.0.1:8000/api/v1/messages`
