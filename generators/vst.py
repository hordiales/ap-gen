# -*- coding: UTF-8 -*-
from iplugingen import PluginGen
from plugincode import PluginCode
from file_utils import copy_file_with_full_path

class Plugin(PluginGen):
	"""
		VST Plugin Generator
	"""

	name = "VST"
	commonDependencies = ['aeffect.h', 'aeffectx.h', 'vstfxstore.h']
	guiDependencies = [] #TODO

	def __init__(self, pluginDef):
		PluginGen.__init__(self, pluginDef)
	#__init_

	def make_sources(self):
		pd = self.pd #plugin definition TODO: take as method argument?

		varsDict = {
			'PluginName': pd.name,
			'PluginNameUpper': pd.name.upper(),
			'ProductString': pd.name,
			'VendorString': pd.copyright,
			'Description': pd.description,
			'Authors': pd.authors,
			'License': pd.license,
			'Category': pd.category,
			'UniqueID': pd.uid,

			'InputsAmount': str(len(pd.inputPorts)),
			'OutputsAmount': str(len(pd.outputPorts)),

			'ControlsDeclaration': "",

			'FilesList': "[ '"+pd.name+".h', '"+pd.name+".cpp' ]"
		}

		pluginFiles = [
		#   (InputTemplateFileName, OutputFile),
			("BaseProcessing.h", pd.name+".h"),
			("BaseProcessing.cpp", pd.name+".cpp"),
			("SConstruct", "SConstruct"),
		]

		for templateName, outputFile in pluginFiles:
			pFile = PluginCode( template=pd.templates_dir+"/vst/"+pd.baseTemplateName+"/%s"%templateName )
			pFile.fillVars( varsDict )
			pFile.write( dir=pd.output_dir+"/"+pd.name, filename=outputFile )

		copy_file_with_full_path( "options.cache", pd.templates_dir+"/vst/"+pd.baseTemplateName, pd.output_dir+"/"+pd.name )
	#make_sources()

	def make_buildsystem(self):
		print "WARNING: vst build system needs to be implemented"
	#make_buildsystem()

	def make_doc(self):
		print "WARNING: vst doc generation needs to be implemented"
	#make_doc()
#class IPlugin
