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
{%PluginName%}::~{%PluginName%} ()
{
	// nothing to do here
}

//-------------------------------------------------------------------------------------------------------
void {%PluginName%}::set_program_name (char* name)
{
	vst_strncpy (programName, name, kVstMaxProgNameLen);
}

//-----------------------------------------------------------------------------------------
void {%PluginName%}::get_program_name (char* name)
{
	vst_strncpy (name, programName, kVstMaxProgNameLen);
}

//-----------------------------------------------------------------------------------------
void {%PluginName%}::set_parameter (VstInt32 index, float value)
{
{%InputControlsSetParam%}
}

//-----------------------------------------------------------------------------------------
float {%PluginName%}::get_parameter (VstInt32 index)
{
{%InputControlsGetParam%}
}

//-----------------------------------------------------------------------------------------
void {%PluginName%}::get_parameter_name (VstInt32 index, char* label)
{
{%InputControlsGetParamName%}
}

//-----------------------------------------------------------------------------------------
void {%PluginName%}::get_parameter_display (VstInt32 index, char* text)
{
{%InputControlsGetParamDisplay%}
}

//-----------------------------------------------------------------------------------------
void {%PluginName%}::get_parameter_label (VstInt32 index, char* label)
{
{%InputControlsGetParamLabel%}
}

//------------------------------------------------------------------------
bool {%PluginName%}::get_effect_name (char* name)
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

//-------------------------------------------------------------------------------------------------------
{%PluginName%}::{%PluginName%} (audioMasterCallback audioMaster)
: AudioEffectX (audioMaster, 1, {%ParametersAmount%}) // 1 program, {%ParametersAmount%} parameter
{
	setNumInputs ({%InputsAmount%}); // stereo in
	setNumOutputs ({%OutputsAmount%}); // stereo out
	
	setUniqueID ('{%PluginName%}');	// identify
	
	canProcessReplacing ();	// supports replacing output
	canDoubleReplacing ();	// supports double precision processing

{%ControlsDefaultValues%}
	vst_strncpy (programName, "Default", kVstMaxProgNameLen);	// default program name
}

//-----------------------------------------------------------------------------------------
void {%PluginName%}::process_replacing (float** inputs, float** outputs, VstInt32 sampleFrames)
{
    //FIXME: take into account mono or stereo case
    float* in1  =  inputs[0];
    float* in2  =  inputs[1];
    float* out1 = outputs[0];
    float* out2 = outputs[1];

	//TODO update parameter values
	
	//passthrough
    while (--sampleFrames >= 0)
    {
        (*out1++) = (*in1++);
        (*out2++) = (*in2++);
    }
}

//-----------------------------------------------------------------------------------------
void {%PluginName%}::process_double_replacing (double** inputs, double** outputs, VstInt32 sampleFrames)
{
    //FIXME: take into account mono or stereo case
    double* in1  =  inputs[0];
    double* in2  =  inputs[1];
    double* out1 = outputs[0];
    double* out2 = outputs[1];

	//TODO update parameter values
// 	double dGain = fGain;
//     while (--sampleFrames >= 0)
//     {
//         (*out1++) = (*in1++) * dGain;
//         (*out2++) = (*in2++) * dGain;
//     }
}
