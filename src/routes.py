from handlers import Handler

handler = Handler()


def setup_routes(app):
    app.router.add_get('/', handler=handler.handle_home)
    app.router.add_get('/greet/{name}', handler=handler.handle_greeting)
    app.router.add_get('/form', handler=handler.handle_form)
    app.router.add_post('/form', handler=handler.handle_form)
