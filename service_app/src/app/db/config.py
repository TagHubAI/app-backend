import os

TORTOISE_ORM_CONFIG = {
    "db_url":os.environ.get("DATABASE_URL"),
    "modules":{"models": ["src.app.db.models", "aerich.models"]},
    "generate_schemas":True,
    "add_exception_handlers":True,
}
