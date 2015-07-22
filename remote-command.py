#!/usr/bin/env python		
# coding: utf8		
import sys,argparse		
import pyjsonrpc
import json		
		
class remote():		
		
	def __init__(self):
		self.clientConnections = [] 		
		#Setup address range to send to 201225		
		'''self.clients = range(201,225)		
		self.clientConnections = []		
		for x in self.clients:		
			self.clientConnections.append(pyjsonrpc.HttpClient(		
			    url = "http://192.168.1.%s:8080" % x,		
			    username = "mininet",		
			    password = "mininet"		
				))	'''	
	
		self.parser = argparse.ArgumentParser()
            #parser.add_argument('integers', metavar='R1 R2', type=int, nargs='2', help='select range of ips like 1 255')               
            #parser.add_argument('v', dest='verbose', action='store_true')              
            	self.parser.add_argument('command', help='command you want to run on remote nodes')
            	self.parser.add_argument('range', default=[], nargs='*')
		self.read_config()



	def read_config(self):
		with open("config.json") as json_file:
	    		json_data = json.load(json_file)
    			print(json_data)
			print 'Options\n======='
			print json_data['options'][0]['name']
			print json_data['options'][1]['name']
			print json_data['options'][2]['name']
			print json_data['options'][3]['name']		
	                self.parser.add_argument('--'+json_data['options'][0]['name'], dest='u'+json_data['options'][0]['name'], default=[],action='store_true')
                        self.parser.add_argument('--'+json_data['options'][1]['name'], dest='u'+json_data['options'][1]['name'], default=[],action='store_true')
                        self.parser.add_argument('--'+json_data['options'][2]['name'], dest='u'+json_data['options'][2]['name'], default=[],action='store_true')
                        self.parser.add_argument('--'+json_data['options'][3]['name'], dest='u'+json_data['options'][3]['name'], default=[],action='store_true')
	                self.args = self.parser.parse_args()
			print "args:"
			print self.args
			if self.args.ubackground:
				print "background"
				for addr in json_data['options'][0]['addresses']:
					self.clientConnections.append(pyjsonrpc.HttpClient(             
                            			url = "http://"+addr+":8080" ))   
			if self.args.u360:
				print "360"
				for addr in json_data['options'][1]['addresses']:
                                        self.clientConnections.append(pyjsonrpc.HttpClient(
                                                url = "http://"+addr+":8080" ))

			if self.args.u720:
				print "720"
				for addr in json_data['options'][2]['addresses']:
                                        self.clientConnections.append(pyjsonrpc.HttpClient(
                                                url = "http://"+addr+":8080" ))

			if self.args.u1080:
				print "1080"
				for addr in json_data['options'][3]['addresses']:
                                        self.clientConnections.append(pyjsonrpc.HttpClient(
                                                url = "http://"+addr+":8080" ))


	def run(self):		
	    self.args = self.parser.parse_args()		
	    print self.args		
	    response = ""		
	    for connection in self.clientConnections:
		print connection.url		
	    for connection in self.clientConnections:		
	    	print 'Sending to %s' % connection.url		
	    	response = connection.call("do_command", self.args.command)		
	#	connection.notify("do_command", self.args.command)	
	    print response
		
    		
remote().run()		
		
		
			
# Notifications send messages to the server, without response.		
#http_client.notify("do_command", "touch hello.txt") 		
