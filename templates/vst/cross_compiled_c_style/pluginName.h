//-------------------------------------------------------------------------------------------------------
// VST Plug-Ins SDK
// Version 2.4
//
// Category     : {%Category%}
// Filename     : {%PluginName%}
// Created by   : {%Authors%}
// Description  : {%Description%}
//
//-------------------------------------------------------------------------------------------------------

#ifndef __{%PluginNameLower%}__
#define __{%PluginNameLower%}__

#include "public.sdk/source/vst2.x/audioeffectx.h"

{%InputControlsEnum%}

class {%PluginName%} : public AudioEffectX
{
public:
	{%PluginName%} (audioMasterCallback audioMaster);
	~{%PluginName%} ();

	//TODO: hacer inline?
	
	// Processing
	virtual void processReplacing (float** inputs, float** outputs, VstInt32 sampleFrames) {
		process_replacing(inputs,outputs,sampleFrames);
	}
	virtual void processDoubleReplacing (double** inputs, double** outputs, VstInt32 sampleFrames) {
		process_double_replacing(inputs,outputs,sampleFrames);
	}

	// Program
	virtual void setProgramName (char* name) { set_program_name(name); }
	virtual void getProgramName (char* name) { get_program_name(name); }

	// Parameters
	virtual void setParameter (VstInt32 index, float value) { set_parameter(index,value); }
	virtual float getParameter (VstInt32 index) { return get_parameter(index); }
	virtual void getParameterLabel (VstInt32 index, char* label);
	virtual void getParameterDisplay (VstInt32 index, char* text);
	virtual void getParameterName (VstInt32 index, char* text);

	virtual bool getEffectName (char* name);
	virtual bool getVendorString (char* text);
	virtual bool getProductString (char* text);
	virtual VstInt32 getVendorVersion ();

protected:
	void process_replacing (float** inputs, float** outputs, VstInt32 sampleFrames);
 	void process_double_replacing (double** inputs, double** outputs, VstInt32 sampleFrames);

	// Program
	void set_program_name (char* name);
	void get_program_name (char* name);

	// Parameters
	void set_parameter (VstInt32 index, float value);
	float get_parameter (VstInt32 index);
// 	void getParameterLabel (VstInt32 index, char* label);
// 	void getParameterDisplay (VstInt32 index, char* text);
// 	void getParameterName (VstInt32 index, char* text);
// 
// 	bool getEffectName (char* name);
// 	bool getVendorString (char* text);
// 	bool getProductString (char* text);
// 	VstInt32 getVendorVersion ();
protected:
{%ControlsDeclaration%}
	char programName[kVstMaxProgNameLen + 1];
};

#endif
