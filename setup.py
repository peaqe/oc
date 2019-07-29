import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

# Get long description from README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

setup(
    name='oc',
    version='0.2.1',
    license='Apache License',
    description='OpenShift CLI (oc) thin wrapper library for Python3',
    long_description=readme,
    author='Rudá Moura',
    author_email="rmoura@redhat.com",
    packages=find_packages(include=['oc']),
    install_requires=['pexpect'],
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries',
    ],
    url='https://github.com/peaqe/oc/',
)
