*******
AnChiPy
*******
.. image:: https://img.shields.io/github/license/mashape/apistatus.svg
   :target:  https://github.com/liang-chen/AnChiPy/blob/master/LICENSE

This application is aimed to convert simplified Chinese text into formatted (classical) document.

==========
Dependency
==========

This package is dependent on `reportlab 3.3.0`_ and `PyPDF2 1.24`_.

.. _reportlab 3.3.0: https://pypi.python.org/pypi/reportlab/3.3.0
.. _PyPDF2 1.24: https://pypi.python.org/pypi/PyPDF2/1.24

============
Installation
============

.. code-block:: bash
    
    $ git clone MY_ANCHIPY_PACKAGE
    $ python setup.py install --install-scripts=/usr/local/bin

=====
Usage
=====

Type your text into a txt file, and use **AnChiPy** to format and generate the PDF. For instance,

.. code-block:: bash

    $anchipy examples/ltjx.txt  

The default output is **anchipy_formatted.pdf**.

=============
DOCUMENTATION
=============
Please see the documentation `here <http://liang-chen.github.io/AnChiPy>`_. 

=======
LICENCE
=======
MIT License

===========
Contributor
===========
`Liang Chen <chen348@indiana.edu>`_
