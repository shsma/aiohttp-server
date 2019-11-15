from handlers import Handler


handler = Handler()

def setup_routes(app):
    app.router.add_get('/', handler.handle_intro)
    app.router.add_get('/greet/{name}', handler.handle_greeting)