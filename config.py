
#wol_hosts = {
#    "srv"       : "00:27:0e:30:28:19",
#    "xps"       : "00:27:0e:1f:32:21",
#    "mediapc"   : "00:27:0e:31:2b:13",
#}

wol_hosts = [
    {
      "name": "srv", 
      "mac": "18:03:73:b0:39:f5",
      "ip": "192.168.0.254",
      "mgt_type": "freenas_api",
    },
    {
      "name": "xps",
      "mac": "00:27:0e:1f:32:21",
      "ip": "192.168.0.36",
      "mgt_type": "ssh_sudo"
    },
    {
      "name": "mediapc",
      "mac": "84:2b:2b:b1:71:b6",
      "ip": "192.168.0.72",
      "mgt_type": "ssh_sudo_nopwd"
    },
]


def get_wol_host(host):
    for wh in wol_hosts:
        if wh['name'] == host:
            break
    return wh
    
    
    
