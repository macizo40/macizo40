#this practice we will create a package that is going to be distributed in the internet and can be adopted.
#the name setup is from the setup tools from python that is the one on charge of the distribution
#and this will have all the configuration of the  distribuable package.
#lest start importing setup package

from setuptools import setup

#to start we will have a method called setup
setup(
    name='Messages',
    version='1.0',
    description='Package to say hello',
    author='macizo40',
    author_email='macizo40@gmail.com',
    url='https://www.macizo40.com',
    packages=['messages'],
    scripts=['modules-test.py']  
)