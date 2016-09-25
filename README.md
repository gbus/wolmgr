# wolmgr

Wolmgr is a web application for managing power on/off of hosts on the local network.
It is based on Cherrypy to provide a restfull interface to send wol, ping or shutdown commands.
The commands are run by the fabric library. 

Power On:

Hosts are set to be started through wake on lan.


Power Off:

For each type of host a plugin is called to handle the specific shutdown procedure:

- freenas_api: shutdown a freenas box by using its restfull API
- ssh_sudo(not implemented yet): to run a shutdown command through ssh

The above should be able to manage any host running freenas, linux, MacOS. There is no plan to implment plugins for other OSes.

Status check:

A ping is run periodically to show when the machine completed the power up/down.


Interface:

The interface is a simple web page based on JS, Ajax, JQuery and bootstrap to call the web application through REST actions.


Installation pre-requisite:

cherrypy
fabric

Installation:

git clone https://github.com/gbus/wolmgr.git


Configuration:

Edit config.py to set the details of the hosts to control (name, IP, MAC, type).
Set the account info for the shutdown plugins in credentials.py.

The package is meant to be run in a linux environment, ideally on a credit card size board, like raspberry pi to keep the power consumption to a minuimum for a system supposed to be permanently on.
