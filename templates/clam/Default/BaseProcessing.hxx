#ifndef _{%ProcessingName%}_
#define _{%ProcessingName%}_

{%INCLUDES%}

namespace CLAM {

	/**
	 *	\brief {%ProcessingName%}
	 *
	 *	{%Description%}
	 */
	class {%ProcessingName%}: public {%BaseProcessing%}
	{	
		/** This method returns the name of the object
		 *  @return Char pointer with the name of object
		 */
		const char *GetClassName() const { return "{%ProcessingName%}"; }
		
		/** Ports **/
		{%Ports%}

		/** Controls **/
		{%Controls%}

	public:
		{%ProcessingName%}(const Config & config=Config())
			{%ConstructorDefaultInit%}
		{
			Configure( config );

			{%ConstructorContent%}
		}

 		~{%ProcessingName%}() {}

		bool Do()
		{
			bool result = Do( {%DoParameters%} );

			{%ConsumeAndProduce%}

			return result;
		}
	
		bool Do({%DoParametersDeclaration%})
		{

			//PUT YOUR SIGNAL PROCESSING CODE HERE

			return true;
		}

	private:

		/** Child processings **/

	};	
	
};//namespace CLAM

#endif // _{%ProcessingName%}_

