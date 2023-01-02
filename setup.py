import setuptools
from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='qomohub',
    version='0.0.3',
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
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.7',
)
