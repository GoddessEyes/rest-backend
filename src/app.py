from fastapi import FastAPI
from fastapi_admin.factory import app as admin_app
from fastapi_admin.site import Site
from src.endpoints.users.routes import router
from src.settings import tortoise_config
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise


def init_admin(app: FastAPI):
    @app.on_event("startup")
    async def startup():
        admin_app.init(
            admin_secret="Shelter",
            permission=True,
            site=Site(
                name="Shelter",
                login_footer="Shelter Admin",
                login_description="Администрация бункера",
                locale="ru",
                locale_switcher=False,
                theme_switcher=False,
            ),
        )


def init_db(app: FastAPI):
    """
    Init database models.
    :param app:
    :return:
    """
    register_tortoise(
        app=app,
        modules=tortoise_config.modules,
        db_url=tortoise_config.db_url,
        generate_schemas=tortoise_config.generate_schemas,
        add_exception_handlers=True,
    )


def __init_app__():
    app = FastAPI()
    init_db(app)
    init_admin(app=app)
    app.mount("/admin", admin_app)
    app.include_router(router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


def init_app():
    app = __init_app__()
    return app
