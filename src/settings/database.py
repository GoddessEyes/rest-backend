import os


TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": os.getenv("POSTGRES_DB", "localhost"),
                "port": os.getenv("POSTGRES_USER", "5432"),
                "user": os.getenv("POSTGRES_PASSWORD", "shelter"),
                "password": os.getenv("POSTGRES_HOST", "shelter"),
                "database": os.getenv("POSTGRES_PORT", "shelter"),
            },
        },
    },
    "apps": {
        "admin": {
            "models": ["admin.models", "aerich.models"],
            "default_connection": "default",
        },
        "users": {
            "models": ["users.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
