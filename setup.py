#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import io
import os

from setuptools import setup

from rest_framework_vault import __version__ as VERSION


def read_req(req_file):
    with open(os.path.join("requirements", req_file)) as req:
        return [
            line.strip()
            for line in req.readlines()
            if line.strip() and not line.strip().startswith("#")
        ]


with io.open("README.md", encoding="utf-8") as readme:
    description = readme.read()

requirements = read_req("base.txt")

setup(
    name="django-rest-vault",
    version=VERSION,
    install_requires=requirements,
    packages=["rest_framework_vault"],
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
