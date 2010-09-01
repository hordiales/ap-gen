# -*- coding: utf-8 -*-

from iplugingen import PluginGen
from plugincode import PluginCode
#from file_utils import make_file, copy_file, make_license_text
from file_utils import copy_file, make_license_text
import time
import sets
import re
#import sys

class Plugin(PluginGen):
	"""
		CLAM Plugin Generator
	"""

	name = "CLAM"
	def __init__(self, pluginDef):
		PluginGen.__init__(self, pluginDef)
		self.definitions_dict = self.load_old_clam_definitions()
	#__init__()

	def make_sources(self):
		self.log_init();
		
		self.make_base_processing_hxx_file(self.definitions_dict)
		self.make_base_processing_cxx_file(self.definitions_dict)

		self.log_end();
	#make_sources()

	def make_buildsystem(self):
		if self.pd.buildSystem=="Scons":
			self.make_sconstruct_file(self.definitions_dict)
			copy_file( self.definitions_dict, "options.cache" )
		else:
			raise Exception("Makefile for CLAM needs to be implemented")
	#make_buildsystem()

	def make_doc(self):
		self.make_readme_file(self.definitions_dict)
	#make_doc()

	def load_old_clam_definitions(self):
		"""
			Method for back compatibility with older implementation, allows to reuse old code until
			the refactoring takes effect
		"""

#TODO: refactor and deprecate all this (definitions_dict is inherited from the old implementation)
# Replace all definitions_dict instances by self.pd.[property] (pd -> plugin definition)

		definitions_dict = {}
	
		definitions_dict['inputs'] = list()
		for dictItem in self.pd.inputPorts:
			definitions_dict['inputs'].append( (dictItem['Type'], dictItem['Name']) )

		definitions_dict['outputs'] = list()
		for dictItem in self.pd.outputPorts:
			definitions_dict['outputs'].append( (dictItem['Type'], dictItem['Name']) )

		definitions_dict['incontrols'] = list()
		definitions_dict['incontrolsfloat'] = list()
		for dictItem in self.pd.inputControls:
			definitions_dict['incontrols'].append( (dictItem['Type'], dictItem['Name']) )
			if dictItem['Type']=="InControlFloat":
				definitions_dict['incontrolsfloat'].append( (dictItem['Min'], dictItem['Max'], dictItem['Name']) )

		definitions_dict['outcontrols'] = list()
		definitions_dict['outcontrolsfloat'] = list()
		for dictItem in self.pd.outputControls:
			definitions_dict['outcontrols'].append( (dictItem['Type'], dictItem['Name']) )
			if dictItem['Type']=="OutControlFloat":
				definitions_dict['outcontrolsfloat'].append( (dictItem['Min'], dictItem['Max'], dictItem['Name']) )

		definitions_dict['plugin_name'] = self.pd.name
		definitions_dict['description'] = self.pd.description
		definitions_dict['authors'] = self.pd.authors
		definitions_dict['category'] = self.pd.category
		definitions_dict["copyright_holder"] = "" # default value
		
		definitions_dict["base_class_name"] = "BaseProcessing"
		definitions_dict["member_style"] = "m" # 'm' or '_' for example
		
		definitions_dict["license"] = "null" # default value
		definitions_dict["year"] = str(time.localtime()[0])

		#now this is splitted
		definitions_dict['license_text'] = make_license_text(definitions_dict)

		#TODO: move these definitions to an upper level of abstraction
		#definitions_dict['standard_name'] = "BaseProcessing"
		definitions_dict['template_name'] = self.pd.baseTemplateName
		definitions_dict['template_dir'] = "templates/clam/"+self.pd.baseTemplateName #dir name
		#definitions_dict['templates_dir'] = '' #TODO: take from config file (ap-gen.conf)
		#definitions_dict["output_dir"] = "../../plugins"  #TODO: take from config file (ap-gen.conf)
		definitions_dict["output_dir"] = self.pd.output_dir

		return definitions_dict
	#load_old_clam_definitions()

	def make_include(self, class_name):
		return "#include <CLAM/" + class_name + ".hxx>\n"
	#make_include()

	def make_base_processing_hxx_file(self, definitions_dict):
		""" BaseProcessing.hxx file """
		
		inputs = definitions_dict["inputs"]
		outputs = definitions_dict["outputs"]
		incontrols = definitions_dict["incontrols"]
		incontrolsfloat = definitions_dict["incontrolsfloat"]
		outcontrols = definitions_dict["outcontrols"]
		outcontrolsfloat = definitions_dict["outcontrolsfloat"]

		member_style = definitions_dict["member_style"] # usually '_' or 'm' as prefix

		#TODO: move BaseProcessing.hxx to configurable filename? (or ready any file name *.hxx from the template folder)
		hxxCode = PluginCode( template=definitions_dict["template_dir"]+"/BaseProcessing.hxx" )

		varsDict = dict()
		varsDict['BaseProcessing'] = "Processing"
		varsDict['ProcessingName'] = definitions_dict["plugin_name"]
		varsDict['Description'] = definitions_dict["description"]

		#Includes#
		varINCLUDES = self.make_include( "Processing" )
		available_port_types_set = sets.Set( (item[0] for item in inputs+outputs) )
		for class_name in available_port_types_set:
			varINCLUDES += self.make_include(class_name)
		if len(incontrols)>0: varINCLUDES += self.make_include("InControl")
		if len(outcontrols)>0: varINCLUDES += self.make_include("OutControl")
		varsDict['INCLUDES'] = varINCLUDES[:-1]
	
		#Ports
		varPorts = ""
		for port_type,port_name in (inputs+outputs):
			if member_style=='_': port_name = port_name[0].lower()+port_name[1:]
			varPorts += "\t\t" + port_type + " " + member_style + port_name.replace(' ', '') + ";\n"
		varsDict['Ports'] = varPorts[2:-1]

		#Controls
		varControls = ""
		for control_type,control_name in (incontrols+outcontrols):
			varControls += "\t\t"+ control_type + " " + member_style + control_name.replace(' ', '') + ";\n"
		varsDict['Controls'] = varControls[2:-1]
	
		#Constructor#
		members_list = []
		for port_type,port_name in (inputs+outputs):
			members_list.append( "\t\t\t" + member_style + port_name.replace(' ', '') + "(\"" + port_name + "\", this)" )
		for control_type,control_name in (incontrols+outcontrols):
			members_list.append( "\t\t\t" + member_style + control_name.replace(' ', '') + "(\"" + control_name + "\", this)" )
		if len(members_list)>0:
			varConstructorDefaultInit = ":\n"
			for i in range(len(members_list)-1):
				varConstructorDefaultInit += members_list[i] + ",\n"
			varConstructorDefaultInit +=  members_list[len(members_list)-1]
		varsDict['ConstructorDefaultInit'] = varConstructorDefaultInit		

		#InControls SetBounds, SetDefaultValue, DoControl#
		varConstructorContent = ""
		for cmin,cmax,control_name in incontrolsfloat:
			control_media = round((float(cmin)+float(cmax))/2.)
			varConstructorContent += "\t\t\t" +  member_style + control_name.replace(' ', '') + ".SetBounds(" + cmin + "," + cmax + ");\n"
			varConstructorContent += "\t\t\t" +  member_style + control_name.replace(' ', '') + ".SetDefaultValue(" + str(control_media) + ");\n"
			varConstructorContent += "\t\t\t" +  member_style + control_name.replace(' ', '') + ".DoControl(" + str(control_media) + ");\n"
		varsDict['ConstructorContent'] = varConstructorContent[3:-1]
	
		varDoParameters = ""
		for port_type,port_name in (inputs+outputs):
			if re.match(".*Audio.*", port_type): varDoParameters += member_style+port_name.replace(' ','')+".GetAudio(), "
#			TODO: implement corresponding method to other types
		varsDict['DoParameters'] = varDoParameters[:-2]

		varConsumeAndProduce = ""
		for port_type,port_name in inputs: varConsumeAndProduce += "\t\t\t"+member_style+port_name.replace(' ','')+".Consume();\n"
		for port_type,port_name in outputs: varConsumeAndProduce += "\t\t\t"+member_style+port_name.replace(' ','')+".Produce();\n"
		varsDict['ConsumeAndProduce'] = varConsumeAndProduce[3:-1]

		varDoParametersDeclaration = ""
		for port_type,port_name in inputs:
			if re.match(".*Audio.*", port_type): varDoParametersDeclaration += "const Audio& in"+port_name.replace(' ','').lower()+", "
#			TODO: implement corresponding method to other types
		for port_type,port_name in outputs:
			if re.match(".*Audio.*", port_type): varDoParametersDeclaration += "Audio& out"+port_name.replace(' ','').lower()+", "
#			TODO: implement corresponding method to other types
		varsDict['DoParametersDeclaration'] = varDoParametersDeclaration[:-2]

		hxxCode.fillVars( varsDict )

		hxxCode.write( dir=definitions_dict["output_dir"]+"/"+self.pd.name, filename=self.pd.name+".hxx" )
	#make_base_processing_hxx_file()

	def make_base_processing_cxx_file(self, definitions_dict):
		""" BaseProcessing.cxx file """

		cxxCode = PluginCode( template=definitions_dict["template_dir"]+"/BaseProcessing.cxx" )

		varsDict = dict()
		varsDict['ProcessingName'] = definitions_dict["plugin_name"]
		varsDict['ProcessingNameLowerCase'] = definitions_dict["plugin_name"].lower()
		varsDict['Description'] = definitions_dict["plugin_name"] #Note: is the plugin_name (and not the real description) since is the text that shows the processing tree...
		varsDict['Category'] = definitions_dict["category"]

		cxxCode.fillVars( varsDict )

		cxxCode.write( dir=definitions_dict["output_dir"]+"/"+definitions_dict["plugin_name"], filename=definitions_dict["plugin_name"]+".cxx" )
	#make_base_processing_cxx_file()

	def make_sconstruct_file(self, definitions_dict):
		""" CLAM standard SConstruct file """

		sconstructFile = PluginCode( template=definitions_dict["template_dir"]+"/SConstruct" )

		varsDict = dict()
		varsDict['ProcessingNameLowerCase'] = definitions_dict["plugin_name"].lower()

		sconstructFile.fillVars( varsDict )

		sconstructFile.write( dir=definitions_dict["output_dir"]+"/"+definitions_dict["plugin_name"], filename="SConstruct" )
	#make_sconstruct_file()

	def make_readme_file(self, definitions_dict):
		""" Standard README file """

		readmeFile = PluginCode( template=definitions_dict["template_dir"]+"/README" )

		varsDict = dict()
		varsDict['Description'] = definitions_dict["description"]
		varsDict['Authors'] = definitions_dict["authors"]

		readmeFile.fillVars( varsDict )

		readmeFile.write( dir=definitions_dict["output_dir"]+"/"+definitions_dict["plugin_name"], filename="README" )
	#make_readme_file()
#class clamPlugin

