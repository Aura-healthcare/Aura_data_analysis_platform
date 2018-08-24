from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="hrv_aura",
    version="0.0.1",
    author="Robin Champseix",
    author_email="rchampseix@octo.com",
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