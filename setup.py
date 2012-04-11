#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

f = open('README.rst')
long_description = f.read().strip()
long_description = long_description.split('split here', 1)[1]
f.close()

setup(
    name='pyCaveExplorer',
    version='0.0.1',
    description="Explore the cave.  Learn about circuits!",
    long_description=long_description,
    url='http://github.com/FOSSRIT/pyCaveExplorer',
    #license='what license?',
    classifiers=[
        "Programming Language :: Python :: 2.7",
    ],
    install_requires=[
        ## This actually requires pygame, but it installs very
        ## weirdly when you try it in a virtualenv on Linux.
        #'pygame',
    ],
    #tests_require=['nose'],
    #test_suite='nose.collector',
    packages=['pyCaveExplorer'],
    include_package_data=True,
    zip_safe=False,
    entry_points="""
    [console_scripts]
    explore-the-cave = pyCaveExplorer.main:main
    """
)
