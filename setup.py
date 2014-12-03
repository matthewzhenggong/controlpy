from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='controlpy',
      version='0.0',
      description='Python controls',
      url='http://github.com/markwmuller/controlpy',
      author='Mark Mueller',
      author_email='mwm@mwm.im',
      license='gplv3',
      packages=['controlpy'],
      zip_safe=False)
