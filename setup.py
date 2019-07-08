try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(name = 'peaqeoc',
      version = '0.1',
      author = 'Rudá Moura',
      author_email = "rmoura@redhat.com",
      py_modules = ['oc'],
      install_requires = ['pexpect'],
)
