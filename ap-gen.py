#!/usr/bin/python
# -*- coding: UTF-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

import sys
import re
from string import split
from xml.dom import minidom
from xml.dom.minidom import getDOMImplementation
import generators

Usage = """Usage: ./ap-gen.py AUDIO-PLUGIN-DEF.xml"""

class APluginDef:
	"""
		Contains plugin definition as properties. Parses xml definition in the constructor
	"""

	def __init__(self, xmlDefFile):
		print "Loading %s audio plugin definition file"%xmlDefFile

		#TODO: take from config file (ap-gen.conf)
		self.output_dir = "plugins" 
		self.templates_dir = "templates" 

		xmlDefFile = minidom.parse(xmlDefFile)

		metadata = xmlDefFile.getElementsByTagName("Metadata")[0]
		self.name = metadata.getElementsByTagName("Name")[0].firstChild.data.strip().replace(' ','') # removes all spaces
		self.description = metadata.getElementsByTagName("Description")[0].firstChild.data.strip()
		self.authors = metadata.getElementsByTagName("Authors")[0].firstChild.data.strip()
		self.copyright = metadata.getElementsByTagName("Copyright")[0].firstChild.data.strip()
		self.copyrightYear = metadata.getElementsByTagName("Copyright")[0].attributes["Year"].value.strip()

		try:
			self.license = metadata.getElementsByTagName("License")[0].firstChild.data.strip()
		except:
			self.license = '-' # Default value

		try: #optional element
			self.uid = metadata.getElementsByTagName("UID")[0].firstChild.data.strip() #TODO: remove spaces?
			#WARNING: avoid cast to int, because then there is a text replacement, int( self.uid ) only for LADSPA, as example vst uses text based UniqueID
		except IndexError:
			self.uid = -1 #default value

		try: #optional element
			self.category = metadata.getElementsByTagName("Category")[0].firstChild.data.strip()
		except IndexError:
			self.category = "Plugins" #default value

		try: #optional element
			self.library = metadata.getElementsByTagName("Library")[0].firstChild.data.strip()
		except IndexError:
			self.library = "" #default value
	
#		print self.name, self.description, self.authors, self.copyrightYear

		outputPlugin = xmlDefFile.getElementsByTagName("OutputPlugin")[0]
		self.standard = outputPlugin.attributes["Standard"].value.strip()
		self.buildSystem = outputPlugin.attributes["BuildSystem"].value.strip()
		self.baseTemplateName = outputPlugin.getElementsByTagName("BaseTemplateName")[0].firstChild.data.strip()
		
#		TODO: parsearch CLAM_DefaultConfig
#		if self.standard=='CLAM':
#			self.baseClass = outputPlugin.getElementsByTagName("CLAM_DefaultConfig")

#		print self.standard, self.buildSystem, self.baseTemplateName

		#TODO:
		if self.standard=='VST':
			vst_prefixElem = outputPlugin.getElementsByTagName("VST_DefaultConfig")[0]
			self.vst_prefix = vst_prefixElem.getElementsByTagName("vst_prefix")[0].firstChild.data.strip()
			
		xmlInputs = xmlDefFile.getElementsByTagName("Inputs")[0]
		self.inputPorts = list()
		for xmlport in xmlInputs.getElementsByTagName("Port"):
			self.inputPorts.append( {'Name':xmlport.attributes["Name"].value.strip(), 'Type':xmlport.firstChild.data.strip()} )
		self.inputControls = list()
		for xmlcontrol in xmlInputs.getElementsByTagName("Control"):
			tmpControl = {'Name':xmlcontrol.attributes["Name"].value.strip(), 'Type':xmlcontrol.firstChild.data.strip()}
			try: #optional attributes
				tmpControl['Min'] = xmlcontrol.attributes["Min"].value.strip()
				tmpControl['Max'] = xmlcontrol.attributes["Max"].value.strip()
				tmpControl['DefaultValue'] = xmlcontrol.attributes["DefaultValue"].value.strip()
			except:
				pass
			self.inputControls.append(tmpControl)

		xmlOutputs = xmlDefFile.getElementsByTagName("Outputs")[0]
		self.outputPorts = list()
		for xmlport in xmlOutputs.getElementsByTagName("Port"):
			self.outputPorts.append( {'Name':xmlport.attributes["Name"].value.strip(), 'Type':xmlport.firstChild.data.strip()} )
		self.outputControls = list()
		for xmlcontrol in xmlOutputs.getElementsByTagName("Control"):
			tmpControl = {'Name':xmlcontrol.attributes["Name"].value.strip(), 'Type':xmlcontrol.firstChild.data.strip()}
			try: #optional attributes
				tmpControl['Min'] = xmlcontrol.attributes["Min"].value.strip()
				tmpControl['Max'] = xmlcontrol.attributes["Max"].value.strip()
			except:
				pass
			self.outputControls.append(tmpControl)

#		print "Ports:"
#		for port in self.inputPorts: print port
#		for port in self.outputPorts: print port
#		print "Controls"	
#		for control in self.inputControls: print control
#		for control in self.outputControls: print control

		#Warnings:
		if self.standard=='LADSPA' and self.uid==-1: print "WARNING: there is no ID in the LADSPA plugin definition (required field)."

	#__init__()
#class APluginDef

if __name__ == '__main__':
	
	if len(sys.argv) < 2:
		print "\nBad amount of input arguments\n", Usage, "\n"
		sys.exit(1)

	#TODO: init ap-gen.conf

	try:
		xmlFile = sys.argv[1]
		plugDef = APluginDef(xmlFile)
	except Exception, e:
		print e
		exit(1)
	
	#FIXME: hacer OO (evitar ifs)
#Ej:
#	try:
#		plugin = eval("generators."+plugDef.standard.lower()+".Plugin(plugDef)")
#	catch:
	if plugDef.standard=='CLAM':
		plugin = generators.clam.Plugin(plugDef)
	elif plugDef.standard=='LADSPA':
		plugin = generators.ladspa.Plugin(plugDef)
	elif plugDef.standard=='VST':
		plugin = generators.vst.Plugin(plugDef)

	plugin.make_all()
#	plugin.make_sources()
#__main__

