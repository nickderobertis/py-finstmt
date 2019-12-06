.. pypi-sphinx-quickstart documentation master file, created by
   pypi-sphinx-quickstart.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Quick Start Example documentation!
*********************************************

Some intro text. To get started, look here.

.. toctree::
   :caption: Tutorial

   tutorial
   auto_examples/index
   blocktypes

An overview
===========

Quick Links
------------

Find the source code `on Github <https://github.com/whoopnip/pypi-sphinx-quickstart>`_.


My Module
------------

Some highlighted functionality from my module.


This is a simple example:

.. code:: python

    import py_qs_example

    obj = py_qs_example.mymodule.ExampleClass(5, int)
    print('done')

.. autosummarynameonly::

      py_qs_example.mymodule.ExampleClass
      py_qs_example.mymodule.example_function

My Package
----------------

.. autosummary::

      py_qs_example.mypackage.module.ExampleClass2
      py_qs_example.mypackage.module.example_function2


.. toctree:: api/modules
   :caption: API Documentation
   :maxdepth: 3

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
