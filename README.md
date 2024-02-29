Quick start
1. git clone https://github.com/Alina200220/gazprom_test.git
2. docker-compose build
3. docker-compose up
4. api server is listen at http://localhost:8000/docs

Описание стурктуры
1. Файл services.py содержит подключение к базе данных (SQLite)
2. Файл models.py содержит модель базы данных, которая влючает в себя информацию об устройствах
3. Файл schemas.py содержит схему модели
4. Файл crud.py содержит функции для загрузки данных в БД, чтения данных о девайсе по id и по временной метке
5. Файл main.py - основной файл приложения
6. Файл requirements.txt включает в себя все зависимости, необходимые для запуска приложения
