*******
AnChiPy
*******

This application is aimed to convert the plain simplified Chinese text into vertically formatted (a.k.a ancient style) Traditional Chinese *literature*.

==========
Dependency
==========

This package is dependent on `Python Imaging Library`_ (PIL), `Jianfan 0.0.2`_, and using the `cxTeX fonts`_.

.. _Jianfan 0.0.2: https://pypi.python.org/pypi/Jianfan
.. _Python Imaging Library: https://pypi.python.org/pypi/PIL
.. _cxTex fonts: https://github.com/l10n-tw/cwtex-q-fonts

============
Installation
============

.. code-block:: bash
    
    $ git clone MY_ANCHIPY_PACKAGE
    $ python setup.py install --user

Add a line to your ~/.bashrc to make it executable

.. code-block:: bash

    alias anchipy='/PATH_TO_PYTHON/bin/anchipy'
    
pip installation unavailable yet...

=====
Usage
=====

Type your Chinese writings into a text file (in either Simplified or Traditional font), and use **AnChiPy** to generate the ancient-style-page (in image format). For instance,

.. code-block:: bash

    $anchipy examples/ltjx.txt  

The default output is **anchipy_formatted.jpg**.

=======
LICENCE
=======
Please see `LICENSE <https://github.iu.edu/chen348/AnChiPy/blob/master/LICENSE>`_.

===========
Contributor
===========
Liang Chen (chen348@indiana.edu)
