# Steps to build a plugin #

  1. Write a XML file with the plugin specifications (see the examples for more info).
  1. Run ap-gen.py against the XML file.
```
ap-gen$ ./ap-gen.py FILE.xml
```
  1. Look for the built files at the 'plugins' directory.

## Examples ##

See the files at 'examples' directory.
```
examples/clam-example-plugin-def.xml
examples/ladspa-example-plugin-def.xml
examples/vst-example-plugin-def.xml
```


**examples/clam-example-plugin-def.xml**:
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE AudioPlugin SYSTEM "AudioPluginDef.dtd">
<AudioPlugin Version="0.1">
	<Metadata>
		<Name>clamTestRtPlugin</Name>
		<Description>This is a test realtime audio CLAM plugin</Description>
		<Authors>Fulano, Sultano, Mengano</Authors>
		<Copyright Year="2010">Club de Audio FIUBA</Copyright>
		<License>GPL</License>
		<Category>Plugins</Category>
	</Metadata>

	<Inputs>
		<Port Name="L Input">AudioInPort</Port>
		<Port Name="R Input">AudioInPort</Port>

		<Control Name="Gain" Min="0." Max="1.0" DefaultValue=".5">FloatInControl</Control>
	</Inputs>
	<Outputs>
		<Port Name="L Output">AudioOutPort</Port>
		<Port Name="R Output">AudioOutPort</Port>
	</Outputs>

	<OutputPlugin Standard="CLAM" BuildSystem="Scons" OS="Linux">
		<BaseTemplateName>Default</BaseTemplateName>

		<CLAM_DefaultConfig> <!--  CLAM plugin specific configuration -->
			<BaseClass>Processing</BaseClass>
			<WithConfig>True</WithConfig>
			<clam_prefix>~/dev/local/clam_dev</clam_prefix> <!-- optional -->
		</CLAM_DefaultConfig>

	</OutputPlugin>
</AudioPlugin>
```

## How to add a new plugin standard generator? ##

  1. Create a new class implementing this interface.
```
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
```

  1. Put the class file at 'generators' directory.
  1. Add the reference to the new plugin generator in the ap-gen.py file.

# Related info #

  * Paper: "[AP-Gen: Framework generador de esqueletos de plugins de audio a partir de abstracciones y templates](http://audiores.uint8.com.ar/files/doc/slides/AP-Gen_%20Framework%20generador%20de%20esqueletos%20de%20plugins%20de%20audio%20a%20partir%20de%20abstracciones%20y%20templates.pdf)" (spanish)
  * Slides: http://www.slideshare.net/hordiales/apgen-slides (spanish)
  * [Blog post](http://audiores.uint8.com.ar/blog/es/2010/09/28/ap-gen-framework-generador-de-esqueletos-de-plugins-de-audio-a-partir-de-abstracciones-y-templates/)  (spanish)