from setuptools import setup

setup(
    name='oc',
    version='0.1.2',
    description='OpenShift CLI (oc) thin wrapper',
    author='Rudá Moura',
    author_email="rmoura@redhat.com",
    py_modules=['oc'],
    install_requires=['pexpect'],
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries',
    ],
)
