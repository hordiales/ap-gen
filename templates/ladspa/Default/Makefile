###############################################################################
#
# Installation DIRECTORIES
#
# Change these if you want to install somewhere else.

INSTALL_PLUGINS_DIR	=	/usr/lib/ladspa/
INSTALL_INCLUDE_DIR	=	/usr/include/
INSTALL_BINARY_DIR	=	/usr/bin/

###############################################################################
#
# GENERAL
#

INCLUDES	=	-I.
LIBRARIES	=	-ldl -lm
CFLAGS		=	$(INCLUDES) -Wall -Werror -O3 -fPIC
CXXFLAGS	=	$(CFLAGS)
CC		=	cc
CPP		=	c++

PLUGIN_NAME = {%PluginName%}
PLUGIN_FILES  =  $(PLUGIN_NAME).c



# C CODE
$(PLUGIN_NAME).so:	$(PLUGIN_FILES) ladspa.h
	$(CC) $(CFLAGS) -o $*.o -c $(PLUGIN_FILES)
	$(LD) -o $(PLUGIN_NAME).so $*.o -shared

# C++ CODE
../plugins/%.so:	plugins/%.cpp ladspa.h
	$(CPP) $(CXXFLAGS) -o $*.o -c $*.cpp
	$(CPP) -o $*.so $*.o -shared


all:	$(PLUGINS)


clean:
	-rm -f `find . -name "*.o"`
	-rm -f `find . -name "*~"`
	-rm $(PLUGIN_NAME).so


