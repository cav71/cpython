.. _cmake-index:

###############################
Building the python interpreter
###############################

This is the documentation for the `CMake <https://cmake.org>`_-based buildsystem.

There are two parts to this document:

    #. instructions for python developer (**Build instructions**)
    #. documenttaion for **extending the build tool itself**

In both cases you need to `download <https://cmake.org/download>`_ and install cmake.


Build instructions
------------------

On Unix, Linux, BSD, macOS, and Cygwin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Native:

.. code-block:: shell-session

    mkdir build
    cd build
      cmake ..
      make

Cross compile Android

.. code-block:: shell-session

    export NDK=<.. location of the ndk>
    mkdir build
    cd build
      cmake \
          -D CMAKE_SYSTEM_NAME=Android \
          -D CMAKE_SYSTEM_VERSION=21 \
          -D CMAKE_ANDROID_NDK=$NDK \
          -D CMAKE_ANDROID_ARCH_ABI=armeabi-v7a \
          ..
      make


On Windows:

.. code-block:: shell-session

    md build
    cd build
      cmake -G "NMake Makefiles" ..
      nmake


Extending the buildtool system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The cmake base buildtool can be adapted and extended using the cmake syntax:

.. toctree::
   :maxdepth: 2

   cmake-modules


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
