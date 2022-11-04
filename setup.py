from setuptools import setup, find_packages
from typing import List

#Declaring variables for setup function
PROJECT_NAME="housing-predictor"
VERSION = "0.0.3"
AUTHOR = "Rashmi"
DESCRIPTION = "This is first machine-learning project"
REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description:this function is going to return list of requirements
    mentioned in requirements.txt

    return:it returns list which contains names of required libraries mentioned in requirements.txt
    """
    
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")



setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()

)

