#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/6 15:41
# @Author  : Weiqiang.long
# @Site    : 
# @File    : setup.py
# @Software: PyCharm
# @Description:

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "dada_openapi_client",
    version = "0.0.1",
    keywords = ("pip", "dada", "openapi", "dadasdk", "dadasign"),
    description = "达达签名数据封装",
    long_description = "dada-sign sdk for python",
    license = "MIT Licence",
    url = "https://www.cnblogs.com/longweiqiang",
    author = "Weiqiang.long",
    packages = setuptools.find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["hashlib"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]

)