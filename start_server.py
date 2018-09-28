import argparse
import chatbot_config as conf
from logger import *
import tornado.web
from handlers import Handler
import tornado
import sys
import os


def create_application():
    return tornado.web.Application([
        (r"/v/?(?P<version>[^\/]+)?/?(?P<module>[^\/]+)?/(?P<action>[^\/]+)",
         Handler.ServiceHandler),
        (r"/",
         Handler.ServiceHandler)
    ], debug=False)


def start_server(port):
    application = create_application()
    settings = {
        'default_handler_class': Handler.ErrorHandler,
        'default_handler_args': dict(status_code=404),
    }
    server = tornado.httpserver.HTTPServer(application,settings)
    server.bind(port)
    logger.info("Server Started at port %s", port)
    server.start(1)
    tornado.ioloop.IOLoop.current().start()


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', help="add the port number on which you want to start the server")
    args = parser.parse_args()
    if args.port is None:
        # if the port number is not given start the server on default 8000 port
        args.port = conf.port
    logger.info("port number is %s", args.port)
    start_server(args.port)