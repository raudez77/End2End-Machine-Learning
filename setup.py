from pathlib import Path
import setuptools
from setuptools import find_packages 

# https://docs.python.org/3/distutils/setupscript.html
# meta - data
NAME = "tid-classification_model"
DESCRIPTION = "Example End to End Machine Learning"
AUTHOR = "Marvin G & Credit to Machine Learning Deployment Udemy Course -ChristopherGS-"
AUTHOR_EMAIL = "raudez@hotmail.com , ChristopherGS:christopher.samiullah@protonmail.com"
REQUIRES_PYTHON = ">=3.7.4"

about = {}
# == Main folder Location ==
ROOT_DIR = Path(__file__).resolve().parent
REQUIREMENTS_DIR = ROOT_DIR / 'requirements'
PACKAGE_DIR = ROOT_DIR / 'classification_model'

with open(PACKAGE_DIR/ "VERSION") as file:
    _version = file.read().strip()
    about["__version__"] = _version

# == Requirements ==
def list_reqs (fname='requirements.txt'):
    with open(REQUIREMENTS_DIR / fname) as file:
        return file.read().splitlines()

# == Setup ==

setuptools.setup (
    name = NAME,
    version = about["__version__"],
    description = DESCRIPTION,
    long_description_content_type = "text/markdown",
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    python_requires = REQUIRES_PYTHON,
    packages = find_packages(),
    package_data= {'classification_model':["VERSION"]},
    install_requires = list_reqs(),
    extras_require = {},
    include_package_data=True,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy"],
)
    
