from config import *
import requests
from wol_credentials import wol_credentials

def freenas_api_shutdown(host):
    ip = get_wol_host(host)['ip']

    try:
        requests.post(
          'http://%s/api/v1.0/system/shutdown/' % ip,
          auth=(wol_credentials[host]["user"], wol_credentials[host]["pwd"]),
        )
        failed = False
        
    except:
        failed = True
    return failed
    
def ssh_sudo_shutdown(host):
    failed = True
    return failed
