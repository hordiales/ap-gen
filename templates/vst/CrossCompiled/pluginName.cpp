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

#include "{%PluginName%}.h"

//-------------------------------------------------------------------------------------------------------
AudioEffect* createEffectInstance (audioMasterCallback audioMaster)
{
	return new {%PluginName%} (audioMaster);
}

//-------------------------------------------------------------------------------------------------------
{%PluginName%}::{%PluginName%} (audioMasterCallback audioMaster)
: AudioEffectX (audioMaster, 1, 1)	// 1 program, 1 parameter only
{
	setNumInputs (2);		// stereo in
	setNumOutputs (2);		// stereo out
	setUniqueID ('Gain');	// identify
	canProcessReplacing ();	// supports replacing output
	canDoubleReplacing ();	// supports double precision processing

	fGain = 1.f;			// default to 0 dB
	vst_strncpy (programName, "Default", kVstMaxProgNameLen);	// default program name
}

//-------------------------------------------------------------------------------------------------------
{%PluginName%}::~{%PluginName%} ()
{
	// nothing to do here
}

//-------------------------------------------------------------------------------------------------------
void {%PluginName%}::setProgramName (char* name)
{
	vst_strncpy (programName, name, kVstMaxProgNameLen);
}

//-----------------------------------------------------------------------------------------
void {%PluginName%}::getProgramName (char* name)
{
	vst_strncpy (name, programName, kVstMaxProgNameLen);
}

//-----------------------------------------------------------------------------------------
void {%PluginName%}::setParameter (VstInt32 index, float value)
{
	fGain = value;
}

//-----------------------------------------------------------------------------------------
float {%PluginName%}::getParameter (VstInt32 index)
{
	return fGain;
}

//-----------------------------------------------------------------------------------------
void {%PluginName%}::getParameterName (VstInt32 index, char* label)
{
	vst_strncpy (label, "Gain", kVstMaxParamStrLen);
}

//-----------------------------------------------------------------------------------------
void {%PluginName%}::getParameterDisplay (VstInt32 index, char* text)
{
	dB2string (fGain, text, kVstMaxParamStrLen);
}

//-----------------------------------------------------------------------------------------
void {%PluginName%}::getParameterLabel (VstInt32 index, char* label)
{
	vst_strncpy (label, "dB", kVstMaxParamStrLen);
}

//------------------------------------------------------------------------
bool {%PluginName%}::getEffectName (char* name)
{
	vst_strncpy (name, "Gain", kVstMaxEffectNameLen);
	return true;
}

//------------------------------------------------------------------------
bool {%PluginName%}::getProductString (char* text)
{
	vst_strncpy (text, "Gain", kVstMaxProductStrLen);
	return true;
}

//------------------------------------------------------------------------
bool {%PluginName%}::getVendorString (char* text)
{
	vst_strncpy (text, "Steinberg Media Technologies", kVstMaxVendorStrLen);
	return true;
}

//-----------------------------------------------------------------------------------------
VstInt32 {%PluginName%}::getVendorVersion ()
{ 
	return 1000; 
}

//-----------------------------------------------------------------------------------------
void {%PluginName%}::processReplacing (float** inputs, float** outputs, VstInt32 sampleFrames)
{
    float* in1  =  inputs[0];
    float* in2  =  inputs[1];
    float* out1 = outputs[0];
    float* out2 = outputs[1];

    while (--sampleFrames >= 0)
    {
        (*out1++) = (*in1++) * fGain;
        (*out2++) = (*in2++) * fGain;
    }
}

//-----------------------------------------------------------------------------------------
void {%PluginName%}::processDoubleReplacing (double** inputs, double** outputs, VstInt32 sampleFrames)
{
    double* in1  =  inputs[0];
    double* in2  =  inputs[1];
    double* out1 = outputs[0];
    double* out2 = outputs[1];
	double dGain = fGain;

    while (--sampleFrames >= 0)
    {
        (*out1++) = (*in1++) * dGain;
        (*out2++) = (*in2++) * dGain;
    }
}
