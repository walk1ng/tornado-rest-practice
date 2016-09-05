#!/usr/bin/env python
# coding:utf-8

from tornado import ioloop
import tornado.httpserver
from tornado.options import define, options, parse_command_line
import config
from motorengine import connect

define('port', group='Webserver', type=int, default=8081, help='run on the given port')

def main():
    parse_command_line()
    
    # connect to mongodb
    io_loop = ioloop.IOLoop.instance()
    connect(config.DB_NAME, host=config.DB_HOST, port=config.DB_PORT, io_loop=io_loop)

    # start the application
    from application import app

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print('Server is running at http://127.0.0.1:{}'.format(options.port))
    print('Quit the server with Control-C')

    # start the ioloop
    io_loop.start()

if __name__ == "__main__":
    main()
