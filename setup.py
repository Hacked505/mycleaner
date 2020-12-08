#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright © 2020 Aleksandr Suvorov
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
# Email: myhackband@yandex.ru
# Github: https://github.com/mysmarthub/mycleaner/
# PyPi: https://pypi.org/project/mycleaner/
# -----------------------------------------------------------------------------
from setuptools import setup, find_packages
from os.path import join, dirname

PACKAGE = "mycleaner"
VERSION = __import__(PACKAGE).__version__
AUTHOR = __import__(PACKAGE).__author__
AUTHOR_EMAIL = "myhackband@yandex.ru"
DESCRIPTION = "Console utility for wiping, zeroing, deleting files." \
              " Aleksandr Suvorov | myhackband@yandex.ru | Donate: 4276 4417 5763 7686"
NAME = "mycleaner"
URL = "https://github.com/mysmarthub/mycleaner"
LICENSE = 'MIT'
LONG_DESCRIPTION = open(join(dirname(__file__), 'README.md')).read()
INSTALL_REQUIRES = []
PLATFORM = ['Linux, Windows']
CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
KEYWORDS = [
    'mycleaner',
    'shred files',
    'zero files',
    'del files',
    'cleaner',
    'smart cleaner',
    'smartcleaner',
    'shred',
    'my cleaner',
    'aleksandr suvorov',
    'smart py',
    'hack band'
]
setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    description=DESCRIPTION,
    version=VERSION,
    license=LICENSE,
    platforms=PLATFORM,
    packages=find_packages(),
    long_description_content_type='text/markdown',
    long_description=LONG_DESCRIPTION,
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
    zip_safe=False,
    keywords=KEYWORDS,
    entry_points={
        'console_scripts':
            ['mycleaner = mycleaner.term_my_cleaner:main']
        }
)
