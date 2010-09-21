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
#			'PluginNameUpper': pd.name.upper(),
#			'ProductString': pd.name,
#			'VendorString': pd.copyright,
			'Description': pd.description,
			'Authors': pd.authors,
			'License': pd.license,
#			'Category': pd.category,
			'UniqueID': pd.uid,

			'InputsAmount': str(len(pd.inputPorts)),
			'OutputsAmount': str(len(pd.outputPorts)),

#FIXME
#			'ControlsDeclaration': "",

			'FilesList': "[ '"+pd.name+".h', '"+pd.name+".cpp' ]"

		pluginFiles = [
		#   (InputTemplateFileName, OutputFile),
			("BaseProcessing.h", pd.name+".h"),
			("BaseProcessing.c", pd.name+".c"),
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
