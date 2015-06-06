# -*- coding: utf-8 -*-
 
 
"""setup.py: setuptools control."""
 
 
import re
from setuptools import setup
 
version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('anchipy/anchipy.py').read(),
    re.M
    ).group(1)
 
 
with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")
 
 
setup(
    name = "cmdline-anchipy",
    packages = ["anchipy"],
    entry_points = {
        "console_scripts": ['anchipy = anchipy.anchipy:main']
        },
    version = version,
    description = "Automatic Ancient Chinese Style Typesetting.",
    long_description = long_descr,
    author = "Liang Chen",
    author_email = "chen348@indiana.edu",
    install_requires=[
          'PIL','jianfan','pypdf2'
      ],
    url = "",
    include_package_data = True,
    package_data = {
        # If any package contains *.ttf files, include them:
        '': ['*.ttf'],
    }
)
