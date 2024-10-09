from setuptools import setup, find_packages
from typing import List
def get_requirements(file_path:str)->List[str]:
    '''
    Returns all requirements
    '''
    hypen_e_dot = "-e ."
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    if hypen_e_dot in requirements:
        requirements.remove(hypen_e_dot)
    return requirements

setup( 
    name='MLProject_Structure', 
    version='0.1', 
    description='A Python project Structure', 
    author='Atharva', 
    author_email='nagarsekaratharva@gmail.com', 
    packages=find_packages(), 
    install_requires=get_requirements("requirements.txt")
) 