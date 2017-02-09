== Intro ==

AP-Gen: Generador de código base de plugins de audio a partir de definiciones
de alto nivel de abstracción.

== Descripción ==

AP-Gen agiliza y facilita el desarrollo de plugins generando código fuente de
base, tanto para diferentes estándares como para diferentes sistemas
operativos, logrando de esta forma que el desarrollador pueda concentrarse en
su objetivo, el procesamiento de audio.

Para lograrlo, parte una serie de definiciones normalizadas y hace uso de un
motor de templates. Estas definiciones pueden ser abstracciones generales del
plugin, como ser cantidad y tipo de entradas y salidas de datos o controles,
o pueden ser más específicas, como cuestiones relativas al sistema de
construcción, metadata y detalles de cada arquitectura. Los templates, por otro
lado, son los elementos que conservan las características comunes de cada
estándar.

La ventaja de esta forma de trabajo se haya en que una vez establecidas las
propiedades de alto nivel, el paso siguiente ya puede ser el de implementar la
función de procesamiento. Dejando de lado, entre otras cosas, el trabajo
mecánico de escribir código de librerías, detalles del lenguaje o estándar de
turno, y cuestiones de compilación de cada arquitectura.

Permite el agregado modular de nuevos estándares.

Licencia: GPL.

Origen: El proyecto nace como una extensión del TemplatedPluginsGenerator
programado inicialmente para CLAM
(http://clam-project.org/clam/trunk/CLAM/scripts/TemplatedPluginsGenerator)

== Dependencias ==

  * 2.5 < Python < 3.0

== Agradecimientos ==

Agradecimientos al proyecto CLAM y su comunidad y al Club de Audio de la FIUBA.

== Links ==

 * AP-Gen: http://code.google.com/p/ap-gen/
 * CLAM (C++ Audio Framework): http://clam-project.org/ 
 * Club de Audio de la FIUBA: http://groups.google.com/group/club_de_audio_fiuba/
