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

{%ControlsDefaultValues%}
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
{%InputControlsSetParam%}
}

//-----------------------------------------------------------------------------------------
float {%PluginName%}::getParameter (VstInt32 index)
{
{%InputControlsGetParam%}
}

//-----------------------------------------------------------------------------------------
void {%PluginName%}::getParameterName (VstInt32 index, char* label)
{
{%InputControlsGetParamName%}
}

//-----------------------------------------------------------------------------------------
void {%PluginName%}::getParameterDisplay (VstInt32 index, char* text)
{
{%InputControlsGetParamDisplay%}
}

//-----------------------------------------------------------------------------------------
void {%PluginName%}::getParameterLabel (VstInt32 index, char* label)
{
{%InputControlsGetParamLabel%}
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
VstInt32 VstXSynth::processEvents (VstEvents* ev)
{
	for (VstInt32 i = 0; i < ev->numEvents; i++)
	{
		if ((ev->events[i])->type != kVstMidiType)
			continue;

		VstMidiEvent* event = (VstMidiEvent*)ev->events[i];
		char* midiData = event->midiData;
		VstInt32 status = midiData[0] & 0xf0;	// ignoring channel
		if (status == 0x90 || status == 0x80)	// we only look at notes
		{
			VstInt32 note = midiData[1] & 0x7f;
			VstInt32 velocity = midiData[2] & 0x7f;
			if (status == 0x80)
				velocity = 0;	// note off by velocity 0
			if (!velocity && (note == currentNote))
				noteOff ();
			else
				noteOn (note, velocity, event->deltaFrames);
		}
		else if (status == 0xb0)
		{
			if (midiData[1] == 0x7e || midiData[1] == 0x7b)	// all notes off
				noteOff ();
		}
		event++;
	}
	return 1;
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
