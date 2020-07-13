![CI](https://github.com/shelter-team/rest-backend/workflows/CI/badge.svg)

## Инструкция для разработки:
1) Склонировать проект себе.
2) Создать .env в корне проекта заполнить аналогично `environments/.env.example`.
3) Подгрузить переменные окружение `pipenv shell` или указать для процесса через плагин.
4) Запустить `postgres` из файла `docker/docker-compose-dev.yml`. `docker-compose -f docker/docker-compose-dev.yaml up`.
5) Запустить приложение `uvicorn src.main:app --reload`.
6) Перед каждым пушем делаем `make lint`.

#### Параметры приложения:

|       Ключ        |     Значение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`DEBUG`| Режим отладки |`True`|


#### Параметры подключения к PostgreSQL:

|       Ключ        |     Значение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`POSTGRES_DB`| Имя БД | `shelter` |
|`POSTGRES_USER`| Пользователь БД | `shelter` |
|`POSTGRES_PASSWORD`| Пароль пользователя БД | `shelter` |
|`POSTGRES_HOST`| Адрес СУБД | `localhost` |
|`POSTGRES_PORT`| Порт СУБД | `5432` |
