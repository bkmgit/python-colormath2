.. _density:

.. include:: global.txt

ANSI and ISO Density
====================

Density may be calculated from
:py:class:`LabColor <colormath2.color_objects.SpectralColor>` instances.

.. autofunction:: colormath2.density.auto_density

.. autofunction:: colormath2.density.ansi_density

Example
-------

.. code-block:: python

    from colormath2.color_objects import SpectralColor
    from colormath2.density import auto_density, ansi_density
    from colormath2.density_standards import ANSI_STATUS_T_RED

    # Omitted the full spectral kwargs for brevity.
    color = SpectralColor(spec_340nm=0.08, ...)
    # ANSI T Density for the spectral color.
    density = auto_density(color)

    # Or maybe we want to specify which filter to use.
    red_density = ansi_density(color, ANSI_STATUS_T_RED)

Valid Density Constants
-----------------------

The following density constants within :py:mod:`colormath2.density_standards`
can be passed to :py:func:`colormath2.density.ansi_density`:

* ``ANSI_STATUS_A_RED``
* ``ANSI_STATUS_A_GREEN``
* ``ANSI_STATUS_A_BLUE``
* ``ANSI_STATUS_E_RED``
* ``ANSI_STATUS_E_GREEN``
* ``ANSI_STATUS_E_BLUE``
* ``ANSI_STATUS_M_RED``
* ``ANSI_STATUS_M_GREEN``
* ``ANSI_STATUS_M_BLUE``
* ``ANSI_STATUS_T_RED``
* ``ANSI_STATUS_T_GREEN``
* ``ANSI_STATUS_T_BLUE``
* ``TYPE1``
* ``TYPE2``
* ``ISO_VISUAL``
