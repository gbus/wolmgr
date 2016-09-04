import os, os.path
import cherrypy
from config import wol_hosts

class WolMgr(object):
   @cherrypy.expose
   def index(self):
       return open('index.html')
       
class WolAPI(object):
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return cherrypy.session['mystring']
        
    def PUT(self, another_string):
        cherrypy.session['mystring'] = another_string
        
        
if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/host': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    webapp = WolMgr()
    webapp.host = WolAPI()
    cherrypy.quickstart(webapp, '/', conf)
