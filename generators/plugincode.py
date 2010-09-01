# -*- coding: utf-8 -*-
import os
import re

class PluginCode:
	""" Plugin code generator helper """
	#TODO: rename the class to PluginCodeGenHelper?

	def __init__(self, template):
		self.code = open(template,'r').read()
	#__init__()

	def write(self, dir, filename):
		if not os.path.isdir(dir): os.mkdir(dir)
		with open( dir+'/'+filename, 'w' ) as f:
			f.write( self.code )
	#write()

#	def replace(self, var, content): self.code = self.code.replace(var,content)

	def fillVars(self, varsDict):
		patternVar = re.compile('{%(?P<var>[^%{}$]+)%}') # {%VARIABLE%}
		result = patternVar.findall( self.code )
		try:
			for var in result:
				#print var,varsDict[var]
				self.code = self.code.replace( '{%'+var+'%}', varsDict[var] )
		except:
			pass
	#fillVars()

#class PluginCode

