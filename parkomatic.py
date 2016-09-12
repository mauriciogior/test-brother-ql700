#!/usr/bin/python

import cups
from os import listdir, remove
import  os.path
import urllib2
import sys
import time
from datetime import datetime
from select import select
import ConfigParser

class PassPrinter:
	conn = None
	printer = None
	tmpLocation = "./"

	def __init__(self):
		#Try to create the tmp location if it doesn't exist
		if not os.path.exists(self.tmpLocation):
			os.makedirs(self.tmpLocation)
		
		#Make a connection to the CUPS server
		try:
			self.conn = cups.Connection()
		except:
			print "ERROR: CUPs not available"
			#Sleep for 5 seconds as repeatedly attemping to connect to CUPs seems to make it hard for cups to start initially.
			time.sleep(5)
			sys.exit(1)
			
		printers = self.conn.getPrinters()
		if len(printers) == 0:
			print "ERROR: No printers available"
			time.sleep(5)
			sys.exit(1)

		#Get the first printer in the list
		self.printer = printers.keys()[0]

	def getImage(self):
		filename = "./pass-example.png"
		return filename

	def printFile(self, filename):
		if filename is not False:
			print "PRINT: "+ str(filename) + " [Sent to printer]"
			self.conn.printFile(self.printer, filename, "Test", {"CutMedia": "2"})

	def mainLoop(self):
		self.printFile("./pass-example.png")
		sys.exit(0)


pp = PassPrinter()
pp.mainLoop()
