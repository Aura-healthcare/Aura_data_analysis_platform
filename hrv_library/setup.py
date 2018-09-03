from codecs import open
from os import path
from setuptools import setup, find_packages

# Get long description in READ.md file
with open("README.md", "r") as fh:
    long_description = fh.read()

#directory = path.abspath(path.dirname(__file__))

# Download and installs dependencies
#with open(path.join(directory, 'requirements.txt'), encoding='utf-8') as req:
#    requirements = req.read().split('\n')

# Mettre que ce dont on a besoin
# tout reinstaller, pour voir racines

setup(
    name="hrvanalysis",
    version="0.0.1",
    author="Robin Champseix",
    author_email="robin.champseix@gmail.com",
    description="a package to calculate features from Rr Interval for HRV analyses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aura-healthcare/Aura_data_analysis_platform",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)