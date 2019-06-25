#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tlturk',
      url='https://github.com/jpowerj/textlab_mturk_api',
      version='0.0.1',
      description='TextLab\'s MTurk API, tlturk: An attempt to make AMT\'s horrific API slightly easier to use from within Python',
      author='Jeff Jacobs, TextLab, Columbia University',
      author_email='jpj2122@columbia.edu',
      packages=['tlturk'],
      install_requires=['requests'],
      license='LICENSE.txt',
    )