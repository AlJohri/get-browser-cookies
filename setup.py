#!/usr/bin/env python3

from setuptools import setup, find_packages

readme = open('README.md').read()
version = exec(open('get_browser_cookies/version.py').read())

setup(
    name='get-browser-cookies',
    version=__version__,
    description='CLI for .',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Al Johri',
    author_email='al.johri@gmail.com',
    url='https://github.com/AlJohri/get-browser-cookies',
    license='MIT',
    packages=find_packages(),
    install_requires=['browser_cookie3'],
    entry_points={
        'console_scripts': [
            'get-browser-cookies=get_browser_cookies.cli:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
    ]
)
