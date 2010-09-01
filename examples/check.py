#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re, subprocess

if __name__ == '__main__':
	xmlfilere = re.compile(".*\.xml$")
	statusOK = True
	for file in os.listdir("."):
		if xmlfilere.match(file):
			try:		
				fileUrl = "./"+file
				process = subprocess.Popen( "xmllint --valid --noout %s"%fileUrl, stdout=subprocess.PIPE, shell=True )
				process.wait()
				output = process.stdout.read().strip()
				if process.returncode!=0:
					raise Exception( "xmllint error in file %s: %s"%(file,output) )
			except Exception, e:
				statusOK = False
				print "Error with audio plugin definition file %s. %s"%(file,e)
	if statusOK: print "Status: OK"
