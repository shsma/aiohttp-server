from aiohttp import web
import aiohttp_jinja2


@aiohttp_jinja2.template('index.jinja2')
async def index(request):
    return {'name': 'shady', 'lastname': 'smaoui'}


@aiohttp_jinja2.template('form.jinja2')
async def form(request):
    return {}


async def web_response(request):
    name = request.match_info.get('name', "Anonymous")
    txt = "Hello, {}".format(name)
    return web.Response(text=txt)