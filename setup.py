#!/usr/bin/env python

from setuptools import setup
# python setup.py sdist bdist_wheel
# python setup.py register -r pypi
# sudo twine upload -s dist/mfnbc-1

long_description = open('README.rst').read()


setup(
    name='mfnbc',
    version='1.97',
    license='The MIT License (MIT)',
    author="Shawn",
    author_email='shawnzam@gmail.com',
    url='https://github.com/shawnzam/mfnbc',
    packages=['mfnbc'],
    install_requires=['nltk>=3.2'],
    keywords=['bayes, nbc, likelihoods', 'posteriors'],
    zip_safe=False,
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering :: Information Analysis'
    ]
)
