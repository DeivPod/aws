from setuptools import setup

setup(
  name='snapshottool',
  version='0.1.0',
  author='Deividas',
  packages=['snapshottool'],
  url='https://github.com/DeivPod/aws/snapshottool',
  license='LICENSE.txt',
  description='EC2 snapshot creator',
  long_description=open('README.txt').read(),
  install_requires=[
    "Click",
    "boto3",
    "unzip"
    "AWS CLI v2"
  ],
)
