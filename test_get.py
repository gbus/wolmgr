import cherrypy
from config import wol_hosts

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
         'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
         'tools.sessions.on': True,
         'tools.response_headers.on': True,
         'tools.response_headers.headers': [('Content-Type', 'text/plain')],
     }
 }
 cherrypy.quickstart(WolWebService(), '/', conf)
