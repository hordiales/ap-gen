# -*- coding: UTF-8 -*-
from iplugingen import PluginGen
from plugincode import PluginCode
from file_utils import copy_file_with_full_path

class Plugin(PluginGen):
	"""
		LADSPA Plugin Generator
	"""

	name = "LADSPA"
	commonDependencies = ['ladspa.h']

	def __init__(self, pluginDef):
		PluginGen.__init__(self, pluginDef)
	#__init_

	def make_sources(self):
		pd = self.pd #plugin definition TODO: take as method argument?

		varsDict = {
			'PluginName': pd.name,
			'PluginPrefix': 'PLUGIN',
			'ShortPluginName': pd.name.strip().replace(' ',''),
			'Label': pd.name.strip().replace(' ','').lower(),
			'FileName': pd.name+'.c',
			'Description': pd.description,
			'Version': '0.1', #TODO: take from xml?
			'Authors': pd.authors,
			'Contact': '', #pd.contact FIXME
			'License': pd.license,
			'LicenseAbastract': '', #FIXME (example GPL for .h and .cpp files)
#			'Category': pd.category,
			'Year': '', #pd.year, #FIXME
			'UniqueID': pd.uid,

			'InputsAmount': str(len(pd.inputPorts)),
			'OutputsAmount': str(len(pd.outputPorts)),

			'ControlInputsAmount': str(len(pd.inputControls)),
			'ControlOutputsAmount': str(len(pd.outputControls)),
			'ControlDefaultValue': "0.1", #TODO: define in the xml, see ['ControlsDeclaration']
#FIXME
#			'ControlsDeclaration': "",

			'FilesList': "[ '"+pd.name+".h', '"+pd.name+".c' ]",
		}

		portNumbers = 0
		varsDict['PortControlNumbers'] = ""
		for i in range(len(pd.inputControls)+len(pd.outputControls)):
			varsDict['PortControlNumbers'] += "#define %s_CONTROL%i %i\n"%(varsDict['PluginPrefix'],i+1,portNumbers)
			portNumbers += 1
		
		varsDict['PortInputNumbers'] = ""
		for i in range(len(pd.inputPorts)):
			varsDict['PortInputNumbers'] += "#define %s_INPUT%i %i\n"%(varsDict['PluginPrefix'],i+1,portNumbers)
			portNumbers += 1
			
		varsDict['PortOutputNumbers'] = ""
		for i in range(len(pd.outputPorts)):
			varsDict['PortOutputNumbers'] += "#define %s_OUTPUT%i %i\n"%(varsDict['PluginPrefix'],i+1,portNumbers)
			portNumbers += 1


		#FIXME
		varsDict['PortsDeclaration'] = "\
			LADSPA_Data * m_pfControl%s;\n\
			LADSPA_Data * m_pfControlComp;\n"%'distortion' #distortion -> conrtol

		#FIXME
		#float (data) controls
		varsDict['ControlsDeclaration'] = ""
		varsDict['ControlsDefaultValues'] = ""
		for dictItem in pd.inputControls:
			if dictItem['Type']=='Data':
				varsDict['ControlsDeclaration'] += "LADSPA_Data %s;\n"%dictItem['Name'].lower()
			varsDict['ControlsDefaultValues'] = "*(ins->m_pfControl%s) = %s;"%(dictItem['Name'].lower(), dictItem['DefaultValue'])

		pluginFiles = [
		#   (InputTemplateFileName, OutputFile),
			("base.c", pd.name+".c"),
			("Makefile", "Makefile"), # TODO: Move makefile code to make_buildsystem()
		]

		for templateName, outputFile in pluginFiles:
			pFile = PluginCode( template=pd.templates_dir+"/ladspa/"+pd.baseTemplateName+"/%s"%templateName )
			pFile.fillVars( varsDict )
			pFile.write( dir=pd.output_dir+"/"+pd.name, filename=outputFile )

		# LADSPA LGPL header 
		copy_file_with_full_path( "ladspa.h", pd.templates_dir+"/ladspa/", pd.output_dir+"/"+pd.name )
		
	#make_sources()

	def make_buildsystem(self):
		# TODO: Move makefile code here
		pass
	#make_buildsystem()

	def make_doc(self):
		print "WARNING: ladspa doc generation needs to be implemented"
	#make_doc()
#class IPlugin
