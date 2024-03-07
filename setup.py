from setuptools import setup,find_packages

E_DOT = '-e .'
required_packages = []
def get_requirements(file_path:str):
    with open(file_path) as file:
        required_packages = file.readlines()
        required_packages = [req.replace("/n","") for req in required_packages]
        if E_DOT in required_packages:
            required_packages.remove(E_DOT)
    return required_packages


setup(
name = 'project1',
version='0.0.1',
author='Sasikumar',
author_email='mssasikumar333@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')
)