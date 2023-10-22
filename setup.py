from setuptools import setup, find_namespace_packages

setup (
    name='DZ_2',
    version='0.0.5',
    description='Very useful code',
    author='Zhang Danil',
    author_email='flyingcircus@example.com',
    classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['greeting = m2.main:greeting']}
)
    
