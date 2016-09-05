# coding:utf-8

from handler.api.base import BaseHandler
from handler.api import errors
from data.collections import User, School

import tornado
from tornado.gen import coroutine
from tornado.web import HTTPError
'''
class RegisterHandler(BaseHandler):
    @tornado.web.asynchronous
    @coroutine
    def post(self):
'''        

class SchoolsHandler(BaseHandler):
    @tornado.web.asynchronous
    @coroutine
    def get(self):
        schools = yield School.objects.find_all()
        print(schools)
        self.write_json([school.to_dict() for school in schools])
