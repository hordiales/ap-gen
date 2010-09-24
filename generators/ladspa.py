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
			'ControlDefaultValue': "0.1", #TODO: define in the xml
#FIXME
#			'ControlsDeclaration': "",

			'FilesList': "[ '"+pd.name+".h', '"+pd.name+".c' ]",
		}

		#FIXME: for i in range(pd.inputPorts+pd.outputPorts+pd.inputControls+pd.outputControls)
		varsDict['PortControlNumbers'] = """
#define DIST_CONTROL 0
#define COMP_CONTROL 1
#define DIST_INPUT 2
#define DIST_OUTPUT 3
"""

		pluginFiles = [
		#   (InputTemplateFileName, OutputFile),
			("base.c", pd.name+".c"),
			("Makefile", "Makefile"),
		]

		for templateName, outputFile in pluginFiles:
			pFile = PluginCode( template=pd.templates_dir+"/ladspa/"+pd.baseTemplateName+"/%s"%templateName )
			pFile.fillVars( varsDict )
			pFile.write( dir=pd.output_dir+"/"+pd.name, filename=outputFile )
#TODO
#		copy_file_with_full_path( "options.cache", pd.templates_dir+"/ladspa/"+pd.baseTemplateName, pd.output_dir+"/"+pd.name )
	#make_sources()

	def make_buildsystem(self):
		print "WARNING: ladspa build system needs to be implemented"
	#make_buildsystem()

	def make_doc(self):
		print "WARNING: ladspa doc generation needs to be implemented"
	#make_doc()
#class IPlugin
