Python Color Math2 Module (colormath2)
======================================

A maintained fork of the unmaintained `python-colormath`_


.. start-badges

|actions|

.. |actions| image:: https://github.com/bkmgit/python-colormath2/workflows/Continuous%20Integration/badge.svg
    :target: https://github.com/bkmgit/python-colormath2/actions
    :alt: Master Build Status

|PyPI|

.. |PyPI| image:: https://badge.fury.io/py/colormath2.svg
    :target: https://badge.fury.io/py/colormath2
    :alt: Latest release on PyPI

|PyPI license|

.. |PyPI license| image:: https://img.shields.io/pypi/l/colormath2.svg
   :target: https://pypi.python.org/pypi/colormath2/
.. end-badges

This module implements a large number of different color operations such as
color space conversions, Delta E, and density to spectral.

Requirements
------------

* Python 3.8+
* `numpy <https://numpy.org/>`_
* `NetworkX <https://networkx.org/>`_ 2.0+

Installation
------------

User Install
^^^^^^^^^^^^

The easiest way to install colormath2 is via pip::

    $ pip install colormath2

Developer Install
^^^^^^^^^^^^^^^^^

Install the development dependencies as follows::

    $ pip install -I -e .[development]

Git and Line Endings
====================

This repo currently uses Windows-style line endings.

If you see ``^M`` at the end of lines in your editor, try running
the following on your local fork::

    git config --local global.whitespace "cr-at-eol"


Documentation
-------------

For documentation, there are currently two main options:

.. list-table::
   :header-rows: 0

   * - This repo's `Examples directory`_
     - Maintained example code for this library

   * - The old `python-colormath docs`_
     - Documentation for the original ``python-colormath``
       module

.. _Examples directory:: https://github.com/pushfoo/python-colormath2/tree/main/examples
.. _python-colormath docs:: http://python-colormath.readthedocs.org/


Support
-------

Head over to https://github.com/bkmgit/python-colormath2
and submit an issue if you have any problems or questions.

Legal Mumbo Jumbo
-----------------

Copyright (C) 2008-2023 `Gregory Taylor`_

Copyright (C) 2024 Benson Muite

This software is licensed under the BSD-3-Clause License.

.. _Gregory Taylor: http://gc-taylor.com
.. _python-colormath: https://github.com/gtaylor/python-colormath
