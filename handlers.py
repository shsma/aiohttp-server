from aiohttp import web
import aiohttp_jinja2

class Handler:

    def __init__(self):
        pass

    @aiohttp_jinja2.template('index.jinja2')
    async def handle_intro(self, request):
        return{'name': 'shady', 'lastname': 'smaoui'}

    async def handle_greeting(self, request):
        name = request.match_info.get('name', "Anonymous")
        txt = "Hello, {}".format(name)
        return web.Response(text=txt)