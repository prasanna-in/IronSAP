import clr
clr.AddReference("System")
clr.AddReference("System.Data")
clr.AddReference("System.Data.SQLite")

import System
from System.Data.SQLite import *
import datetime
import ping as a2
import db as db2
import portscan as ps
from IronWASP import *


class begin():
	def __init__(self, isap):
	 #print "Start"
	 self.isap = isap
	 self.ipadd = self.isap.target
	 if self.isap.perform_attack == True:
	 	GlobalStore.Put("Attack","YES")
	 if self.isap.verbose == True:
	 	GlobalStore.Put("Verbose","YES")
	 if GlobalStore.Get("Attack")=="YES":
	 	self.isap.print_out("Attack Mode : YES",0)
	 if GlobalStore.Get("Verbose")=="YES":
	 	self.isap.print_out("Verbose Mode : YES",0)
	 activeid = 1
	 self.pinghost(activeid)
	 
	 
	def pinghost(self,activeid):
	 ping = a2.PingCheck(self.ipadd,activeid,self.isap)
	 pingres = ping.ping()
	 #Now Lets send the ping results to the database recorder. 
	 dbw = db2.dbwrite(self.isap)
	 dbw.pingwrite(pingres)
	 if pingres[2] == "Success":
	 	self.portscancontroller("Success")
	 else:
	 	self.portscancontroller("Fail")
	
	def portscancontroller(self,result):
		if result=="Success":
			self.isap.print_out("Port Scan Starting please be patient .... ",0)
			self.actid = 1
			portScan = ps.portscan(self.ipadd,self.actid,self.isap)
			portScan.controller()

		else:
			self.isap.print_out("Host Seems to Be DOWN.. Shuting Down.", 1)
	

	 	
	 

	 