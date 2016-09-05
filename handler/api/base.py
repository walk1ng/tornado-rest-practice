# coding:utf-8

from tornado.web import RequestHandler, HTTPError
from handler.api import errors
from bson.json_util import dumps

class BaseHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        RequestHandler.__init__(self, application, request, **kwargs)
        self.set_header('Content-Type', 'text/json')

    def get(self):
        raise HTTPError(**errors.status_0)
   
    def post(self):
        raise HTTPError(**errors.status_0)

    def put(self):
        raise HTTPError(**errors.status_0)

    def delete(self):
        raise HTTPError(**errors.status_0)

    def write_error(self, status_code, **kwargs):
        self.write_json(None, self._status_code, self._reason)

    def write_json(self, data, status_code=200, msg='success'):
        self.finish(dumps({
		'code': status_code,
		'msg': msg,
		'data': data
	}))

class APINotFoundHandler(BaseHandler):
    def get(self):
        raise HTTPError(**errors.status_1)

    def post(self):
        raise HTTPError(**errors.status_1)

    def put(self):
        raise HTTPError(**errors.status_1)
    
    def delete(self):
        raise HTTPError(**errors.status_1)

