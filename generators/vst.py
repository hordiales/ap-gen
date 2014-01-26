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
			'VendorVersion': pd.uid,
			'UniqueID': pd.uid,
			'Description': pd.description,
			'Authors': pd.authors,
			'License': pd.license,
			'Library': pd.library,
			'Category': pd.category,

			'VST_PREFIX': pd.vst_prefix,
		
			'InputsAmount': str(len(pd.inputPorts)),
			'OutputsAmount': str(len(pd.outputPorts)),

			'ParametersAmount': str(len(pd.inputControls)), # VST Parameters
			#'ControlOutputsAmount': str(len(pd.outputControls)),
			
			#TODO: add parameters names, default values, min/max, etc
			
			'ControlsDeclaration': "",
			'ControlsDefaultValues': "", #initial values

			'FilesList': "[ '"+pd.name+".h', '"+pd.name+".cpp' ]",
		}

		#Input Controls
		varsDict['InputControlsSetParam'] = "\tswitch (index)\n\t{\n"
		varsDict['InputControlsGetParam'] = "\tswitch (index)\n\t{\n"
		varsDict['InputControlsGetParamName'] = "\tswitch (index)\n\t{\n"
		varsDict['InputControlsGetParamDisplay'] = "\tswitch (index)\n\t{\n"
		varsDict['InputControlsGetParamLabel'] = "\tswitch (index)\n\t{\n"
		varsDict['InputControlsEnum'] = "enum CONTROL_NAMES {\n"
		for dictItem in self.pd.inputControls:
			#FIXME: input value could not be float (implement for other types) (now if Float disabled)
			#       all variables starts with 'f' of float...
			#       use dictItem['Type'].lower() for general implementation
			#if dictItem['Type']=="Float":
			varsDict['ControlsDeclaration'] += "\t%s f%s;\n"%(dictItem['Type'].lower(),dictItem['Name'].strip())
			#optional attributes
			try:
				varsDict['ControlsDefaultValues'] += "\tf%s = %sf;\n"%(dictItem['Name'].strip(), dictItem['DefaultValue'])
			except:
				pass

			
			varsDict['InputControlsSetParam'] += "\t\tcase k%s : f%s = value; break;\n"%(dictItem['Name'].strip(),dictItem['Name'].strip())
			varsDict['InputControlsGetParam'] += "\t\tcase k%s : return f%s;\n"%(dictItem['Name'].strip(),dictItem['Name'].strip())
			varsDict['InputControlsGetParamName'] += """\t\tcase k%s : vst_strncpy (label, "%s", kVstMaxParamStrLen); break;  \n"""%(dictItem['Name'].strip(),dictItem['Name'].strip())
			#TODO: Could be dB2string or float2string
			varsDict['InputControlsGetParamDisplay'] += """\t\tcase k%s : float2string (f%s, text, kVstMaxParamStrLen); break; \n"""%(dictItem['Name'].strip(),dictItem['Name'].strip())
			varsDict['InputControlsGetParamLabel'] += """\t\tcase k%s : vst_strncpy (label, "%s", kVstMaxParamStrLen); break; \n"""%(dictItem['Name'].strip(),dictItem['Label'].strip())
			
			varsDict['InputControlsEnum'] += "\tk%s,\n"%dictItem['Name'].strip()

		varsDict['InputControlsSetParam'] += "\t}"
		if len(pd.inputControls)==1:
		  varsDict['InputControlsSetParam'] = "\tf%s = value;"%dictItem['Name'].strip()
		varsDict['InputControlsGetParam'] += "\t}"
		if len(pd.inputControls)==1:
		  varsDict['InputControlsGetParam'] = "\treturn f%s;"%dictItem['Name'].strip()
		varsDict['InputControlsGetParamName'] += "\t}"
		if len(pd.inputControls)==1:
		  varsDict['InputControlsGetParamName'] = """\tvst_strncpy (label, "%s", kVstMaxParamStrLen);"""%dictItem['Name'].strip()
		
		varsDict['InputControlsGetParamDisplay'] += "\t}"
		if len(pd.inputControls)==1:
		  varsDict['InputControlsGetParamDisplay'] = """\tfloat2string (f%s, text, kVstMaxParamStrLen);"""%dictItem['Name'].strip()
		varsDict['InputControlsGetParamDisplay'] = """\t//Could be dB2string or float2string\n"""+varsDict['InputControlsGetParamDisplay']
		
		varsDict['InputControlsGetParamLabel'] += "\t}"
		if len(pd.inputControls)==1:
		  varsDict['InputControlsGetParamLabel'] = """\tvst_strncpy (label, "%s", kVstMaxParamStrLen);"""%dictItem['Label'].strip()
		
		
		varsDict['InputControlsEnum'] += "};"

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
