# wolmgr

Wolmgr is a web application for turning hosts on/off  from remote. 
It is based on Cherrypy to provide a restfull interface to send WOL, ping or shutdown commands.
The commands are run by the fabric library (http://www.fabfile.org/). 

<i>Power On:</i>

A wake on lan command is run on the local network.


<i>Power Off:</i>

For each type of host a plugin is called to handle the specific shutdown procedure:

- freenas_api: shutdown a freenas box by using its restfull API
- ssh_sudo(not implemented yet): to run a shutdown command through ssh

The above should be able to manage any host running freenas, linux, MacOS. There is no plan to implment plugins for other OSes.

Status check:

A ping is run periodically to show when the machine completed the power up/down.


<b>Interface:</b>

The interface is a simple web page based on JS, Ajax, JQuery and bootstrap to call the web application through REST actions.


![wolmgr](https://cloud.githubusercontent.com/assets/4559307/19318209/acab2466-909f-11e6-9b4c-a4d4b2f6e512.png)


<b>Installation pre-requisite:</b>

cherrypy
fabric
wakeonline tools

<b>Installation:</b>

git clone https://github.com/gbus/wolmgr.git

on a raspberry pi create a link to the wol command:
 sudo ln /usr/bin/wakeonlan /bin/wol

<b>Configuration:</b>

Rename config.py.example in config.py and edit it as per example (name, IP, MAC, type).
Set the account info for the shutdown plugins in credentials.py.

<b>Security:</b>

The app doesn't currently offer any access protection. I have set up a vpn to limit the access  to the service from remote. In future user/password login will be implemented. 

The package is meant to be run in a linux environment, ideally on a credit card size board, (like raspberry pi) to keep the power consumption to a minuimum for a system supposed to be permanently on.


TODO

- Access to the interface through login
- tool to automatically configure passwordless ssh hosts and power them off
