# coding:utf-8
from handler.api.test import TestHandler
from handler.api.base import APINotFoundHandler
from handler.api.user.register import SchoolsHandler

urls = [
   (r'/test', TestHandler),
   (r'/api/users/schools', SchoolsHandler ),
   (r'.*', APINotFoundHandler)
]
