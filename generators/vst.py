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
			'PluginNameLower': pd.name.lower(),
			'PluginNameUpper': pd.name.upper(),
			'ProductString': pd.name,
			'VendorString': pd.copyright,
			'Description': pd.description,
			'Authors': pd.authors,
			'License': pd.license,
			'Library': pd.library,
			'Category': pd.category,
			'UniqueID': pd.uid,

			'VST_PREFIX': pd.vst_prefix,

			'InputsAmount': str(len(pd.inputPorts)),
			'OutputsAmount': str(len(pd.outputPorts)),

			'ControlsDeclaration': "",
			'ControlsDefaultValues': "", #initial values

			'FilesList': "[ '"+pd.name+".h', '"+pd.name+".cpp' ]",
		}

		for dictItem in self.pd.inputControls:
			if dictItem['Type']=="Float":
				varsDict['ControlsDeclaration'] += "    float f%s;\n"%dictItem['Name'].strip()
				#optional attributes
				try:
					varsDict['ControlsDefaultValues'] += "    f%s = %sf;\n"%(dictItem['Name'].strip(), dictItem['DefaultValue'])
				except:
					pass
		varsDict['ControlsDeclaration'] = varsDict['ControlsDeclaration'][4:] #removing first spaces
		varsDict['ControlsDefaultValues'] = varsDict['ControlsDefaultValues'][4:] #removing first spaces

		pluginFiles = [
		#   (InputTemplateFileName, OutputFile),
			("pluginName.h", pd.name+".h"),
			("pluginName.cpp", pd.name+".cpp"),
			("Makefile", "Makefile"),
			("pluginName.def", pd.name+".def"),
		]

		for templateName, outputFile in pluginFiles:
			pFile = PluginCode( template=pd.templates_dir+"/vst/"+pd.baseTemplateName+"/%s"%templateName )
			pFile.fillVars( varsDict )
			pFile.write( dir=pd.output_dir+"/"+pd.name, filename=outputFile )

		#copy_file_with_full_path( "options.cache", pd.templates_dir+"/vst/"+pd.baseTemplateName, pd.output_dir+"/"+pd.name )
	#make_sources()

	def make_buildsystem(self):
		#TODO: file is already built in make_sources() move it here
		pass
	#make_buildsystem()

	def make_doc(self):
		print "WARNING: vst doc generation needs to be implemented"
	#make_doc()
#class IPlugin
