# SDK version must be 2.4
VSTSDKDIR = {%VST_PREFIX%}

PLUGIN_NAME = {%PluginName%}

CPP       = i586-mingw32msvc-g++

VST_OBJ_COMMON = $(VSTSDKDIR)/public.sdk/source/vst2.x/vstplugmain.o $(VSTSDKDIR)/public.sdk/source/vst2.x/audioeffect.o $(VSTSDKDIR)/public.sdk/source/vst2.x/audioeffectx.o

VST_GUI_OBJ = $(VSTSDKDIR)/vstgui.sf/vstgui/aeffguieditor.o $(VSTSDKDIR)/vstgui.sf/vstgui/vstgui.o $(VSTSDKDIR)/vstgui.sf/vstgui/vstcontrols.o $(VSTSDKDIR)/vstgui.sf/vstgui/cscrollview.o $(VSTSDKDIR)/vstgui.sf/vstgui/ctabview.o 
#$(VSTSDKDIR)/vstgui.sf/vstgui/plugguieditor.o
#$(VSTSDKDIR)/vstgui.sf/vstgui/cfileselector.o

RES_OBJ  = #resources/{%PluginName%}.rc

VST_OBJ = $(VST_OBJ_COMMON) $(VST_GUI_OBJ)
DLL_OBJ = 
OBJ       = $(PLUGIN_NAME).o $(VST_OBJ) $(DLL_OBJ) $(RES_OBJ).o

LIBS      = -L. --add-stdcall-alias -lole32 -lkernel32 -lgdi32 -luuid -luser32 -mwindows --no-export-all-symbols --def $(PLUGIN_NAME).def

CXXINCS   = -I"$(VSTSDKDIR)/pluginterfaces/vst2.x" -I"$(VSTSDKDIR)/public.sdk/source/vst2.x" -I"$(VSTSDKDIR)" -I"$(VSTSDKDIR)/vstgui.sf/vstgui" -I. 
BIN       = $(PLUGIN_NAME).dll
CXXFLAGS  = $(CXXINCS) -DBUILDING_DLL=1 -mwindows -O3
RM        = rm -f

.PHONY: all clean

all: $(PLUGIN_NAME).dll

clean:
	${RM} $(PLUGIN_NAME).o $(VST_OBJ) $(BIN)
	${RM} editor/sdeditor.o

# not we're using mingw dllwrap tool
DLLWRAP   = i586-mingw32msvc-dllwrap

DEFFILE   = lib$(PLUGIN_NAME).def

STATICLIB = lib$(PLUGIN_NAME).a

$(BIN): $(OBJ)
	# note the --driver-name is equal to the compiler executable name for mingw
	$(DLLWRAP) --output-def $(DEFFILE) --driver-name $(CPP) --implib $(STATICLIB) $(OBJ) $(LIBS) -o $(BIN)

%.o: %.cpp
	$(CPP) -c $< -o $@ $(CXXFLAGS)

#$(RES_OBJ).o: $(RES_OBJ)
#	i586-mingw32msvc-windres $(RES_OBJ) $(RES_OBJ).o

$(VSTSDKDIR)/public.sdk/source/vst2.x/vstplugmain.o: $(VSTSDKDIR)/public.sdk/source/vst2.x/vstplugmain.cpp
	$(CPP) -c $(VSTSDKDIR)/public.sdk/source/vst2.x/vstplugmain.cpp -o $(VSTSDKDIR)/public.sdk/source/vst2.x/vstplugmain.o $(CXXFLAGS)

$(VSTSDKDIR)/public.sdk/source/vst2.x/audioeffect.o: $(VSTSDKDIR)/public.sdk/source/vst2.x/audioeffect.cpp
	$(CPP) -c $(VSTSDKDIR)/public.sdk/source/vst2.x/audioeffect.cpp -o $(VSTSDKDIR)/public.sdk/source/vst2.x/audioeffect.o $(CXXFLAGS)

$(VSTSDKDIR)/public.sdk/source/vst2.x/audioeffectx.o: $(VSTSDKDIR)/public.sdk/source/vst2.x/audioeffectx.cpp
	$(CPP) -c $(VSTSDKDIR)/public.sdk/source/vst2.x/audioeffectx.cpp -o $(VSTSDKDIR)/public.sdk/source/vst2.x/audioeffectx.o $(CXXFLAGS)
	
$(VSTSDKDIR)/vstgui.sf/vstgui/aeffguieditor.o: $(VSTSDKDIR)/vstgui.sf/vstgui/aeffguieditor.cpp
	$(CPP) -c $(VSTSDKDIR)/vstgui.sf/vstgui/aeffguieditor.cpp -o $(VSTSDKDIR)/vstgui.sf/vstgui/aeffguieditor.o $(CXXFLAGS)

$(VSTSDKDIR)/vstgui.sf/vstgui/vstgui.o: $(VSTSDKDIR)/vstgui.sf/vstgui/vstgui.cpp
	$(CPP) -c $(VSTSDKDIR)/vstgui.sf/vstgui/vstgui.cpp -o $(VSTSDKDIR)/vstgui.sf/vstgui/vstgui.o $(CXXFLAGS)

$(VSTSDKDIR)/vstgui.sf/vstgui/vstcontrols.o: $(VSTSDKDIR)/vstgui.sf/vstgui/vstcontrols.cpp
	$(CPP) -c $(VSTSDKDIR)/vstgui.sf/vstgui/vstcontrols.cpp -o $(VSTSDKDIR)/vstgui.sf/vstgui/vstcontrols.o $(CXXFLAGS)
	
$(VSTSDKDIR)/vstgui.sf/vstgui/cscrollview.o: $(VSTSDKDIR)/vstgui.sf/vstgui/cscrollview.cpp
	$(CPP) -c $(VSTSDKDIR)/vstgui.sf/vstgui/cscrollview.cpp -o $(VSTSDKDIR)/vstgui.sf/vstgui/cscrollview.o $(CXXFLAGS)
	
$(VSTSDKDIR)/vstgui.sf/vstgui/ctabview.o: $(VSTSDKDIR)/vstgui.sf/vstgui/ctabview.cpp
	$(CPP) -c $(VSTSDKDIR)/vstgui.sf/vstgui/ctabview.cpp -o $(VSTSDKDIR)/vstgui.sf/vstgui/ctabview.o $(CXXFLAGS)

# $(VSTSDKDIR)/vstgui.sf/vstgui/cfileselector.o: $(VSTSDKDIR)/vstgui.sf/vstgui/cfileselector.cpp
# 	$(CPP) -c $(VSTSDKDIR)/vstgui.sf/vstgui/cfileselector.cpp -o $(VSTSDKDIR)/vstgui.sf/vstgui/cfileselector.o $(CXXFLAGS)
	
# $(VSTSDKDIR)/vstgui.sf/vstgui/plugguieditor.o: $(VSTSDKDIR)/vstgui.sf/vstgui/plugguieditor.cpp
# 	$(CPP) -c $(VSTSDKDIR)/vstgui.sf/vstgui/plugguieditor.cpp -o $(VSTSDKDIR)/vstgui.sf/vstgui/plugguieditor.o $(CXXFLAGS)
	
	
