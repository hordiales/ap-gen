Intro
=====

Audio plugins skeleton maker.

Description
===========

AP-Gen speeds up and eases the plugin development through base source code
generation, both for different standards and operating systems, thus achieving
that the developer can focus on his goal, the digital audio processing.

To achieve this, starts from normalized definitions and uses a template engine.
These definitions could be general abstractions of the plugin, like amount and
type of inputs and outputs of data or controls, or more specific ones, like the
kind of the build system, metadata and even details of each architecture. On
the other hand, the templates are the elements that maintain the common
features of each standard.

The advantage of this way of working is that, once high level aspects are
established, next step can be to develop the signal processing function.
Leaving aside, among other things, all the repetitive work of writing library
code, programming language or current standard details, and each architecture
compilation issues.

Support to new standards can be added in a modular form.

INSTALL
=======

Dependencies:
  * Python > 2.5

THANKS
======

CLAM project and Club de Audio FIUBA.

LICENSE
=======

GPL

LINKS
=====

 * AP-Gen: [http://hordiales.github.io/ap-gen](http://hordiales.github.io/ap-gen)
 * CLAM (C++ Audio Framework): [http://clam-project.org/](http://clam-project.org/)
 * Club de Audio de la FIUBA: [http://groups.google.com/group/club_de_audio_fiuba/](http://groups.google.com/group/club_de_audio_fiuba/)
