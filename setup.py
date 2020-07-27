from setuptools import setup, find_packages


def read(filename):
    return [requirement.strip() for requirement in open(filename).readlines()]



setup(
    name="chico_delivery",
    version="0.1.0", #major, minor, patch
    description="chico_delivery_topzeira",
    packeges=find_packages(exclude=".venv"),
    include_package_data=True,
    install_requires=read('requirements.txt'),
    extras_require={
            "dev" : read("requirements-dev.txt")
    }

)