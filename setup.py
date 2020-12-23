"""
daikinapi python module manifest
"""
from os.path import abspath, dirname, join
from setuptools import setup

__version__ = "1.0.6"


def read_file(filename):
    """Get the contents of a file"""
    here = abspath(dirname(__file__))
    with open(join(here, filename), encoding="utf-8") as file:
        return file.read()


setup(
    name="daikinapi",
    version=__version__,
    description="Get metrics from Daikin airconditioning unit wifi module",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    packages=["daikinapi"],
    package_dir={"daikinapi": "."},
    keywords=["Daikin", "airconditioning", "API"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    url="https://github.com/arska/python-daikinapi",
    author="Aarno Aukia",
    author_email="aarno@aukia.com",
    license="MIT",
    python_requires=">=3.5",
    extras_require={"dev": ["tox"]},
    install_requires=["requests>=2", "urllib3>=1.24"],
)
