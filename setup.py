from setuptools import setup, find_packages

setup(
    name='oc',
    version='0.2.0',
    description='OpenShift CLI (oc) thin wrapper',
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
)
