import setuptools
from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='qomohub',
    version='0.0.1',
    packages=setuptools.find_packages(),
    url='https://github.com/davendw49/qomolangma-datahub/',
    license='Apache',
    author='Cheng Deng',
    author_email='davendw@sjtu.edu.cn',
    description='Signal data of Qomolangma (the largest Geoscience Language Model)',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['datalabs'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
        "dataset"
    ],
    python_requires='>=3.7',
)
