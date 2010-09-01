#include "{%ProcessingName%}.hxx"
#include <CLAM/ProcessingFactory.hxx>

namespace CLAM
{

namespace Hidden
{
	static const char * metadata[] = {
		"key", "{%ProcessingNameLowerCase%}",
		"category", "{%Category%}",
		"description", "{%Description%}",
		0
	};
	static FactoryRegistrator<ProcessingFactory, {%ProcessingName%}> reg = metadata;
}

}
