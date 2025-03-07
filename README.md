# [Task here](https://docs.google.com/document/d/1-fvs0LaX2oWPjO6w6Bpglz1Ndy_KrNV7NeNgRlks94k/)

# Comments for task

почта и пароль для моковых пользователей:

    user@example.com
    string

    1user@example.com
    string

В задании указаны разные сущности для *User* и *Admin*. Но эти сущности 
имеют одниаковую авторизацию поэтому они объединены в одну таблицу User 
и различаются лишь флагом "is_admin".

В данном конкретном проекте файл __.env__ не добавлен в __.gitignore__, во исзбежание дублирования информации по запуску приложения, т.к. __.env__ дополняет данные инструкции.

HASH_SALT генерируется модулем __os__:

    import os

    salt = os.urandom(16).hex()

OAUTH_SECRET_KEY получен аналогично HASH_SALT


# Running an Application without Docker
## Dependencies

[Install UV](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1)

[Install Docker Engine](https://docs.docker.com/engine/install/)


Run Postgres(from system installig or from docker)

Change variables in .env for correct connection to Posgres


    alembic upgrade head
    uvicorn --factory main:create_app --host 0.0.0.0 --port 8000

# Running an Application with Docker

Change variables in .env for correct connection to Posgres

Run Docker Compose

    $ docker compose up -d
