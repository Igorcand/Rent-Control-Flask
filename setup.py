from setuptools import setup, find_packages

def read(filename):
    return [req.strip() for req in open(filename).readlines()]

#semantic version(semver.org)
setup(
    name='rental_controller',
    version='0.1.0', #major, minor, patch
    description='Rental Controller app',
    packages=find_packages(exclude='../venv'),
    include_package_data=True,
    install_requires=read('requirements.txt'),
    )

# python setup.py install