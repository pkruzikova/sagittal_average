from setuptools import setup, find_packages

setup(name="Sagittal brain analysis", 
    version="0.1.0", 
    packages=find_packages(exclude=['*tests']),
    entry_points = {'console_scripts': ['sagaverage = sagittal_average.command:process']})
