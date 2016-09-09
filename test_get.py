import cherrypy
from config import wol_hosts
import os, os.path
import json

def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"

class Wol(object):
    @cherrypy.expose
    def index(self):
        return open('pages/index.html')
        
        
class WolWebService(object):
    exposed = True

    @cherrypy.tools.json_out()
    # @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return wol_hosts

#     def POST(self, length=8):
#         some_string = ''.join(random.sample(string.hexdigits, int(length)))
#         cherrypy.session['mystring'] = some_string
#         return some_string
#
#     def PUT(self, another_string):
#         cherrypy.session['mystring'] = another_string
#
#     def DELETE(self):
#         cherrypy.session.pop('mystring', None)

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
            'tools.CORS.on': True,
        },
        '/api': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
            'tools.CORS.on': True,
        },     
    }
    cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
    webapp = Wol()
    webapp.api = WolWebService()
    cherrypy.quickstart(webapp, '/', conf)
