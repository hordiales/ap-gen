AP-Gen speeds up and eases the plugin development through base source code generation, both for different standards and operating systems, thus achieving that the developer can focus on his goal, the digital audio processing.

To achieve this, starts from normalized definitions and uses a template engine. These definitions could be general abstractions of the plugin, like amount and type of inputs and outputs of data or controls, or more specific ones, like the kind of the build system, metadata and even details of each architecture. On the other hand, the templates are the elements that maintain the common features of each standard.

The advantage of this way of working is that, once high level aspects are established, next step can be to develop the signal processing function. Leaving aside, among other things, all the repetitive work of writing library code, programming language or current standard details, and each architecture compilation issues.

Support to new standards can be added in a modular form.

See [Documentation](Documentation.md)


---


AP-Gen agiliza y facilita el desarrollo de plugins generando código fuente de base, tanto para diferentes estándares como para diferentes sistemas operativos, logrando de esta forma que el desarrollador pueda concentrarse en su objetivo, el procesamiento de audio.

Para lograrlo, parte una serie de definiciones normalizadas y hace uso de un motor de templates. Estas definiciones pueden ser abstracciones generales del plugin, como ser cantidad y tipo de entradas y salidas de datos o controles, o pueden ser más específicas, como cuestiones relativas al sistema de construcción, metadata y detalles de cada arquitectura. Los templates, por otro lado, son los elementos que conservan las características comunes de cada estándar.

La ventaja de esta forma de trabajo se haya en que una vez establecidas las propiedades de alto nivel, el paso siguiente ya puede ser el de implementar la función de procesamiento. Dejando de lado, entre otras cosas, el trabajo mecánico de escribir código de librerías, detalles del lenguaje o estándar de turno, y cuestiones de compilación de cada arquitectura.

Permite el agregado modular de nuevos estándares.

[Documentation](Documentation.md)