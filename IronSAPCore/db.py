import clr
clr.AddReference("System")
clr.AddReference("System.Data")
clr.AddReference("System.Data.SQLite")

import System
from System.Data.SQLite import *
import fingerprint
#import httppages
from IronWASP import *
import webservices as ws

class dbwrite():
	
	def __init__(self, isap):
		self.isap = isap
		pass
	def pingwrite(self,values):
		self.isap.print_out("Writing Ping Values To DB\r\n", 0)
		#for x in values:
		#	print x
	def portscanwrite(self,values):
		self.isap.print_out("Writing PortScan Values to DB\r\n", 0)
		self.isap.print_out("Ports Open :\r\n", 1)
		for value in values.iterkeys():
			self.isap.print_out(value+":" + str(values[value]) + "\r\n", 1)
		fp1 = fingerprint.fingerprint(values, self.isap)
		fp1.starts()
		
	def fingerprintwrite(self,response200,response404,response401,values):
		#print response200,response404,response401,values
		#print "Displaying HTML Analysis Results:"
		
		if GlobalStore.Get("Verbose")== "YES":
			self.isap.print_out("Responses for Requests that returned a Response 200:" + str(response200) + "\r\n", 2)
			self.isap.print_out("\r\n", 2)
			self.isap.print_out("Information Gathered from Error Pages:" + str(response404) + "\r\n", 2)
			self.isap.print_out("\r\n", 2)
			self.isap.print_out("Result of Verb Tampering:" + str(response401) + "\r\n", 2)
		#ws = webservices.webservices(values)
		#ws.start()
		 
#		print "Detailed Page Analysis Results:","\n"
#		print pagechecker
		#hp = httppages.httppages()
		#hp.starts()
		
		
		
		
		
		

		

 	