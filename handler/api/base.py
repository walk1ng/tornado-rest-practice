# coding:utf-8

from tornado.web import RequestHandler, HTTPError
from handler.api import errors

class BaseHanlder(RequestHandler):
    def __init__(self, application, request, **kwargs):
        RequestHandler.__init__(self, application, request, **kwargs)
        self.set_header('Content-Type', 'text/json')

    def get(self):
        raise HTTPError(**errors.status_0)

    def put(self):
        raise HTTPError(**errors.status_0)
