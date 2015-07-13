#!/usr/bin/env python
# coding: utf-8
import sys,argparse
import pyjsonrpc

class remote():

	def __init__(self):
		#Setup address range to send to 201-225
			self.clients = range(201,225)
			self.clientConnections = []
			for x in self.clients:
				self.clientConnections.append(pyjsonrpc.HttpClient(
			    url = "http://192.168.1.%s:8080" % x,
			    username = "mininet",
			    password = "mininet"
				))

	def run(self):
	    parser = argparse.ArgumentParser()
	    #parser.add_argument('integers', metavar='R1 R2', type=int, nargs='2', help='select range of ips like 1-255')
	    #parser.add_argument('-v', dest='verbose', action='store_true')
	    parser.add_argument('command', help='command you want to run on remote nodes')
	    parser.add_argument('range', default=[], nargs='*')
	    self.args = parser.parse_args()
	    print self.args
	    response = ""

	    for connection in self.clientConnections:
	    	print 'Sending to %s' % connection.url
	    	response = connection.call("do_command", self.args.command)

	    print response

    
remote().run()


	
# Notifications send messages to the server, without response.
#http_client.notify("do_command", "touch hello.txt")