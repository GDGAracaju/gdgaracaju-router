#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

blog_uri = r"http://blog.gdgaracaju.com.br"

class MainHandler(webapp2.RequestHandler):
    def get(self):
        return self.redirect('http:\/\/site.gdgaracaju.com.br')

class BloggerPageHandler(webapp2.RequestHandler):
    def get(self, page):
    	page_uri = r"%s/p/%s" % (blog_uri, page)
        return self.redirect(page_uri)

class BloggerPostHandler(webapp2.RequestHandler):
    def get(self, year, month, post_name):
    	post_uri = r"%s/%s/%s/%s" % (blog_uri, year, month, post_name)
        return self.redirect(post_uri)

app = webapp2.WSGIApplication([
    webapp2.Route(r'/p/<page>', BloggerPageHandler),
    webapp2.Route(r'/<year>/<month>/<post_name>', BloggerPostHandler),
    webapp2.Route(r'/', MainHandler),
], debug=True)
