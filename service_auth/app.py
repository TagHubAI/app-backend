from fastapi import FastAPI

from easyauth.server import EasyAuthServer
import os

server = FastAPI()

@server.on_event('startup')
async def startup():
    server.auth = await EasyAuthServer.create(
        server,
        '/auth/token',
        auth_secret=os.environ["AUTH_SECRET"],
        admin_title='EasyAuth - Company',
        admin_prefix='/admin',
        env_from_file='server_env.json'
    )

