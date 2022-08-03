from setuptools import setup, find_packages
from typing import List

REQUIREMENT_FILE = 'requirements.txt'
PROJECT_NAME = "house-price-pridictor"
VIRSION = "0.0.4"
AUTHOR = "Pankaj"
DESCRIPTION = "House Price Predictor using Machine Learning"
PACKAGES = ['housing']
# Variables for setup function
def get_requirement_list() -> List[str]:
    """
    Discription: This fucnction is return the list of required 
    package avaible in the requirement.txt file   
    Return: List of library require for the project 
    """
    with open(REQUIREMENT_FILE) as required_file:
        return required_file.readlines().remove("-e .")


setup(
name=PROJECT_NAME,
version=VIRSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires= get_requirement_list()
)

if __name__=='__main__':
    print(get_requirement_list())