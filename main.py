import tornado.ioloop
import tornado.web

from web.handlers.handlers import get_handlers


def make_app():
    return tornado.web.Application(get_handlers())


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
