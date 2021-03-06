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
    name="dada_openapi_client",
    version="1.0.3",
    author="Weiqiang.long",
    description="达达签名数据封装",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/longweiqiang/dada_openapi_python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]

)