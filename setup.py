#!/usr/bin/env python
# -*- coding: utf-8 -*-
import colormath2

from setuptools import setup

LONG_DESCRIPTION = open("README.rst").read()

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Scientific/Engineering :: Mathematics",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
]

KEYWORDS = "color math conversions"

setup(
    name="colormath2",
    version=colormath2.VERSION,
    description="Color math and conversion library.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    author="Gregory Taylor",
    author_email="gtaylor@gc-taylor.com",
    maintainer="Benson Muite",
    url="https://github.com/bkmgit/python-colormath2",
    download_url="http://pypi.python.org/pypi/colormath2/",
    packages=["colormath2"],
    platforms=["Platform Independent"],
    license="BSD-3-Clause",
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    install_requires=["numpy", "networkx>=2.0"],
    extras_require={"development": ["black", "flake8", "nose2", "pre-commit", "sphinx"]},
)
