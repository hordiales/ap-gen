# SDK version must be 2.4
VSTSDKDIR = {%VST_PREFIX%}

PLUGIN_NAME = {%PluginName%}

#CPP       = i586-mingw32msvc-g++ #Target win32
CPP       = i686-w64-mingw32-g++ #Target win32
#CPP = x86_64-w64-mingw32-g++ #Target win64

#DLLWRAP   = i586-mingw32msvc-dllwrap # Target win32, ubuntu <=14 
DLLWRAP   = i686-w64-mingw32-dllwrap --target=i386-mingw32 # Target win32, ubuntu >14
#DLLWRAP	= x86_64-w64-mingw32-dllwrap # Target win64

VST_OBJ = $(VSTSDKDIR)/public.sdk/source/vst2.x/vstplugmain.o $(VSTSDKDIR)/public.sdk/source/vst2.x/audioeffect.o $(VSTSDKDIR)/public.sdk/source/vst2.x/audioeffectx.o

OBJ       = $(PLUGIN_NAME).o $(VST_OBJ)

LIBS      = -L. --add-stdcall-alias -lole32 -lkernel32 -lgdi32 -luuid -luser32 -mwindows -lpthread --no-export-all-symbols --def $(PLUGIN_NAME).def

CXXINCS   = -I"$(VSTSDKDIR)/pluginterfaces/vst2.x" -I"$(VSTSDKDIR)/public.sdk/source/vst2.x" -I"$(VSTSDKDIR)" -I"$(VSTSDKDIR)/vstgui.sf/vstgui" -I.
BIN       = $(PLUGIN_NAME).dll

#CXXFLAGS  = $(CXXINCS) -DBUILDING_DLL=1 -mwindows -O3
#WARNING: adding static dependencies to work in i686, ubuntu >14
CXXFLAGS  = $(CXXINCS) -DBUILDING_DLL=3 -mwindows -O3 -static -static-libgcc -static-libstdc++
#-mfpmath=sse -msse -ffast-math -DBUILDING_DLL -Wno-multichar -Wno-write-strings
RM        = rm -f

.PHONY: all clean

all: $(PLUGIN_NAME).dll

clean:
	${RM} $(OBJ) $(BIN)


DEFFILE   = lib$(PLUGIN_NAME).def

STATICLIB = lib$(PLUGIN_NAME).a

$(BIN): $(OBJ)
	# note the --driver-name is equal to the compiler executable name for mingw
	$(DLLWRAP) --output-def $(DEFFILE) --driver-name $(CPP) --implib $(STATICLIB) $(OBJ) $(LIBS) $(CXXFLAGS) -o $(BIN)

%.o: %.cpp
	$(CPP) -c $< -o $@ $(CXXFLAGS)

$(VSTSDKDIR)/public.sdk/source/vst2.x/vstplugmain.o: $(VSTSDKDIR)/public.sdk/source/vst2.x/vstplugmain.cpp
	$(CPP) -c $(VSTSDKDIR)/public.sdk/source/vst2.x/vstplugmain.cpp -o $(VSTSDKDIR)/public.sdk/source/vst2.x/vstplugmain.o $(CXXFLAGS)

$(VSTSDKDIR)/public.sdk/source/vst2.x/audioeffect.o: $(VSTSDKDIR)/public.sdk/source/vst2.x/audioeffect.cpp
	$(CPP) -c $(VSTSDKDIR)/public.sdk/source/vst2.x/audioeffect.cpp -o $(VSTSDKDIR)/public.sdk/source/vst2.x/audioeffect.o $(CXXFLAGS)

$(VSTSDKDIR)/public.sdk/source/vst2.x/audioeffectx.o: $(VSTSDKDIR)/public.sdk/source/vst2.x/audioeffectx.cpp
	$(CPP) -c $(VSTSDKDIR)/public.sdk/source/vst2.x/audioeffectx.cpp -o $(VSTSDKDIR)/public.sdk/source/vst2.x/audioeffectx.o $(CXXFLAGS)

