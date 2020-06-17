#!/usr/bin/env python

from setuptools import setup


setup(name="ecdsa",
      description="ECDSA cryptographic signature library (pure python)",
      author="Lingfeng Zheng",
      author_email="lingfeng.zheng@alumnosupm.es",
      packages=["ecdsa"],
      license="MIT",
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.2",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
      ],
      install_requires=['six'],
      )
