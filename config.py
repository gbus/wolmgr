
cherrypy_globals = {
    'server.socket_host': '0.0.0.0',
    'server.socket_port': 8080,
}

wol_hosts = [
    {
      "name": "nas", 
      "mac": "18:03:73:b0:39:f5",
      "ip": "192.168.0.254",
      "mgt_type": "freenas_api",
    },
    {
      "name": "desktop",
      "mac": "00:22:19:2c:28:2f",
      "ip": "192.168.0.11",
      "mgt_type": "ssh_sudo"
    },
]


def get_wol_host(host):
    for wh in wol_hosts:
        if wh['name'] == host:
            break
    return wh
    
    
    
