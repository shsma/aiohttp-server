import asyncio
import jinja2
import aiohttp_jinja2
from aiohttp import web
from routes import setup_routes


# load config from yaml file in current dir
# conf = load_config(str(pathlib.Path('.') / 'config' / 'polls.yaml'))
# app['config'] = conf

loop = asyncio.get_event_loop()
app = web.Application(loop=loop)

aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader('templates'))

setup_routes(app)

web.run_app(app, host='127.0.0.1', port=8080)