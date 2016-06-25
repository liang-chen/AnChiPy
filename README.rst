*******
AnChiPy
*******

This application is aimed to convert the plain simplified Chinese text into vertically formatted (a.k.a ancient style) classical Chinese document.

==========
Dependency
==========

This package is dependent on `Python Imaging Library`_ (PIL) and `PyPDF2 1.24`_.

.. _Python Imaging Library: https://pypi.python.org/pypi/PIL
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

Type your Chinese writings into a text file (in either Simplified or Traditional font), and use **AnChiPy** to generate the ancient-style page (in image format). For instance,

.. code-block:: bash

    $anchipy examples/ltjx.txt  

The default output is **anchipy_formatted.pdf**.

=============
DOCUMENTATION
=============
Please see `here <http://liang-chen.github.io/AnChiPy>`_. 

=======
LICENCE
=======
MIT `LICENSE <https://github.com/liang-chen/AnChiPy/blob/master/LICENSE>`_.

===========
Contributor
===========
Liang Chen (chen348@indiana.edu)
