# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Password Generator", # the name that you will install via pip
    version="1.1",
    author="Raymond Huang",
    author_email="dravech.1@gmail.com",
    description="First attempt at a python package that involves generation of passwords",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/alf-faren/Lambdata-faren",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)