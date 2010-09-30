# -*- coding: utf-8 -*-
import os, sys, shutil

def copy_file_with_full_path(filename, from_path, to_path ):
	if os.path.isfile( from_path+"/"+filename ):
		print "Copying " + filename + " file"
		shutil.copyfile( from_path+"/"+filename, to_path+"/"+filename )
#copy_file_with_full_path()

#TODO: below functions needs to be revised
def copy_file( definitions_dict, filename ):
	if os.path.isfile( definitions_dict["template_dir"] + "/" + filename):
		print "Copying " + filename + " file"
		shutil.copyfile( definitions_dict["template_dir"] + "/" + filename, definitions_dict["output_dir"] + "/" + definitions_dict["plugin_name"] + "/" + filename )
#copy_file()

def make_license_text(definitions_dict):
	try:
		f = open( "licenses/" + definitions_dict["license"] + ".txt", 'r' )
	except IOError:
		print "License file read error."
		print "License: " + definitions_dict["license"]
		sys.exit(2)
	license_text = f.read(); f.close()
	if definitions_dict["copyright_holder"]!="":
		license_text = license_text.replace( "Copyright (C)", "Copyright (C) " + definitions_dict["year"] + " " + definitions_dict["copyright_holder"] )
	else:
		license_text = license_text.replace( "Copyright (C)", "" )
	return license_text
#make_license_text()

