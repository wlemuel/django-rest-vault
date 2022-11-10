#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import io
import os
import re

from setuptools import setup


_pkg = "rest_framework_vault"


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, "__init__.py")).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(
        1
    )


with io.open("README.md", encoding="utf-8") as readme:
    description = readme.read()

requirements = [
    "Django>=2.2.16",
    "djangorestframework>=3.10.3",
    "pycryptodome>=3.9.1",
]
VERSION = get_version(_pkg)

setup(
    name="django-rest-vault",
    version=VERSION,
    install_requires=requirements,
    packages=[_pkg],
    include_package_data=True,
    license="MIT License",
    description="Api data decryption and encryption support for Django REST Framework",
    long_description=description,
    long_description_content_type="text/markdown",
    test_suite="tests",
    url="https://github.com/wlemuel/django-rest-vault",
    author="Steve Lemuel",
    author_email="wlemuel@hotmail.com",
    keywords="drf django django-rest-framework",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
