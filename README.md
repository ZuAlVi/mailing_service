Mailing service

- Сервис для автоматической рассылки сообщений по Email.
- Для работы с сервисом необходима регистрация по Email с последующей верификацией.
- Авторизованый пользователь может добавлять электронную почту своих клиентов, создать письмо и рассылку.
- Колличество клиентов рассылки не ограничено.
- Переодичность рассылки настраивается пользователем(разовая, ежедневная, еженедельная, ежемесячная).


Как запустить:

- Необходимо клонировать проект с помощью консольной команды
    `git clone https://github.com/ZuAlVi/mailing_service`
- Войти в виртуальное окружение введя в терминале:
    - в Windows `venv\Scripts\activate.bat`
    - в Linux и MacOS `source venv/bin/activate`
- Установить зависимости из файла requirements.txt
    `pip install requirements.txt`
- Создать в корне проекта файл .env и заполнить его необходимыми данными из файла .env.sample.
- Чтобы создать суперпользователя для доступа в админку необходимо в терминале ввести команду
    `python manage.py csu`
- Чтобы запустить сервис автоматической рассылки необходимо в терминале ввести команду
    `python manage.py runapscheduler`. После этого рассылка будет идти в автоматическом режиме.
- Запустить сервер можно командой в терминале
    `python manage.py runserver`
- Перейти в любом интернет браузере по адресу http://127.0.0.1:8000/ 

