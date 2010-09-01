# -*- coding: UTF-8 -*-

class IPluginGen:
	""" Addon plugin generator public interface """
	def make_all(self): raise Exception("This is an interface with no implementation")
	def make_sources(self): raise Exception("This is an interface with no implementation")
	def make_buildsystem(self):
		"""" Makefile, SConscript files, etc """
		raise Exception("This is an interface with no implementation")
	def make_doc(self):
		""" README file, diagrams, doxygen output generation, etc """
		raise Exception("This is an interface with no implementation")
#interface IPluginGen

class PluginGen:
	""" Addon plugin generator abstract class """
	name = ""
	commonDependencies = []

	def __init__(self, pluginDef):
		self.pd = pluginDef 
	#__init__

	def make_all(self):
		self.make_sources()
		self.make_buildsystem()
		self.make_doc()
	#make_all()

	def make_standard_readme_file(self, extraTxt):
#		TODO: make README file from name, description, etc plus extraTxt
		pass	
	#make_standard_readme_file()

	def log_init(self):
		print "*** Making %s plugin ***"%self.name #TODO: pasar a decorator genérico
		print "Name: %s"%self.pd.name
		print "Description: %s"%self.pd.description
		print "Authors: %s"%self.pd.authors
	#log_init()a

	def log_end(self):
		print "%s plugin finished."%self.pd.name
#		print "See %s for files"%("TODO: poner path final")
	#log_init()

	#private interface#
	def make_include(self, class_name): raise Exception("This is an interface with no implementation")
	def make_base_processing_hxx_file(self, definitions_dict): raise Exception("This is an interface with no implementation")
	def make_base_processing_cxx_file(self, definitions_dict): raise Exception("This is an interface with no implementation")

	def make_sconstruct_file(self, definitions_dict): raise Exception("This is an interface with no implementation")
	def make_readme_file(self, definitions_dict): raise Exception("This is an interface with no implementation")
#class PluginGen

