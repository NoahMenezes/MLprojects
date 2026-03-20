from typing import List

from setuptools import find_packages, setup

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements file and returns a list of package names.
    """
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements


setup(
    name="Mlprojects",
    version="0.0.1",
    author="Noah Menezes",
    author_email="2006noahmenezes@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
