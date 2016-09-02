# coding:utf-8

import tornado.web
import os
from url import urls

app = tornado.web.Application(
	hanlders=urls,
	template_path=os.path.join(os.path.dirname(__file__), 'template'),
	static_path=os.path.join(os.path.dirname(__file__), 'static'),
	debug=True,
	allow_remote_access=True
)
