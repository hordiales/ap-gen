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
: AudioEffectX (audioMaster, 1, {%ParametersAmount%}) // 1 program, 1 parameter only
{
	setNumInputs ({%InputsAmount%}); // stereo in
	setNumOutputs ({%OutputsAmount%}); // stereo out
	
	setUniqueID ('{%PluginName%}');	// identify
	
	canProcessReplacing ();	// supports replacing output
	canDoubleReplacing ();	// supports double precision processing

	//TODO update parameter values
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
	//TODO update parameter values
	fGain = value;
}

//-----------------------------------------------------------------------------------------
float {%PluginName%}::getParameter (VstInt32 index)
{
	//TODO update parameter values
	return fGain;
}

//-----------------------------------------------------------------------------------------
void {%PluginName%}::getParameterName (VstInt32 index, char* label)
{
	//TODO update parameter values
	vst_strncpy (label, "Gain", kVstMaxParamStrLen);
}

//-----------------------------------------------------------------------------------------
void {%PluginName%}::getParameterDisplay (VstInt32 index, char* text)
{
	//TODO update parameter values
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
	//TODO review if PluginName is the best option here
	vst_strncpy (name, "{%PluginName%}", kVstMaxEffectNameLen);
	return true;
}

//------------------------------------------------------------------------
bool {%PluginName%}::getProductString (char* text)
{
	vst_strncpy (text, "{%ProductString%}", kVstMaxProductStrLen);
	return true;
}

//------------------------------------------------------------------------
bool {%PluginName%}::getVendorString (char* text)
{
	vst_strncpy (text, "{%VendorString%}", kVstMaxVendorStrLen);
	return true;
}

//-----------------------------------------------------------------------------------------
VstInt32 {%PluginName%}::getVendorVersion ()
{ 
	return {%VendorVersion%}; 
}

//-----------------------------------------------------------------------------------------
void {%PluginName%}::processReplacing (float** inputs, float** outputs, VstInt32 sampleFrames)
{
    float* in1  =  inputs[0];
    float* in2  =  inputs[1];
    float* out1 = outputs[0];
    float* out2 = outputs[1];

	//TODO update parameter values
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

	//TODO update parameter values
	double dGain = fGain;
    while (--sampleFrames >= 0)
    {
        (*out1++) = (*in1++) * dGain;
        (*out2++) = (*in2++) * dGain;
    }
}