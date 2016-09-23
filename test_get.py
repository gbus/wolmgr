import cherrypy
from config import *
import wol_plugins
import os, os.path
import json
import subprocess
import sys
try:
    from fabric.api import *
#    from wakeonlan import wol
except:
    print "Error: not all required libraries are available"
    sys.exit(-1)
    
    
def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"

class WolMgr(object):
    @cherrypy.expose
    def index(self):
        return open('pages/index.html')
        
        
class WolWebService(object):
    exposed = True

#    @cherrypy.tools.json_out()
#    def GET(self):
#        return wol_hosts
        
    def _cp_dispatch(self, vpath):
        if len(vpath) == 1:
            cherrypy.request.params['host'] = vpath.pop()
            return self

    @cherrypy.tools.json_out()
    def GET(self, host):
        if host == "_all":
            return wol_hosts
            
        ret = { "status" : "NA" }
        
        wh = get_wol_host(host)                
        with settings(warn_only=True):
            ipcheck=local("ping -c 1 -w 3 %s" % wh['ip'], capture=True)
                
        #ipcheck = subprocess.Popen(["/bin/ping", "-c 1", "-w 3", ip], stdout=subprocess.PIPE).wait() 
        # Check cherrypy.session[host]["Request"] to provide extra status info 
        if ipcheck.failed:
            ret["status"] = "Off"
        else:
            ret["status"] = "On"
        return ret

    @cherrypy.tools.json_out()
    def POST(self, host, action):
        ret = { "result" : "NA" }
        
        wh = get_wol_host(host)
        ip          = wh['ip']
        mac         = wh['mac']
        mgt_type   = wh['mgt_type']
        
        if action == "TurnOn":
            #wol.send_magic_packet(mac)
            with settings(warn_only=True):
                wake_host = local( "/bin/wol %s" % mac, capture=True )
            ret["result"] = { "action" : "On", "failed" : wake_host.failed }
            
        elif action == "TurnOff":
#            env.hosts = [ip]
#            with settings(warn_only=True):
#                poweroff = run("poweroff")
            shutdown_func = getattr(wol_plugins, "%s_shutdown" % mgt_type)
            failed = shutdown_func(host)
            ret["result"] = { "action" : "Off", "failed" : failed }
        else:
            ret["result"] = { "action" : "NA", "failed" : True }
        #???cherrypy.session[host]["Request"] = action
        return ret
                
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
    cherrypy.config.update(cherrypy_globals)
    
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
            'tools.CORS.on': True,
        },
        '/wol': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
            'tools.CORS.on': True,
        },   
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        },  
    }
    cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
    webapp = WolMgr()
    webapp.wol = WolWebService()
    cherrypy.quickstart(webapp, '/', conf)
