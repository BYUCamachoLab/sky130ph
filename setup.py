import pathlib

from gdsfactory.install import _install_to_klayout
from setuptools import find_packages, setup

with open("README.md") as f:
    LONG_DESCRIPTION = f.read()


def get_install_requires():
    with open("requirements.txt") as f:
        return [line.strip() for line in f.readlines() if not line.startswith("-")]


setup(
    name="sky130ph",
    version="0.0.5",
    url="https://github.com/joamatab/cookiecutter-pypackage-minimal",
    license="MIT",
    author="SkandanC",
    author_email="s39chand@uwaterloo.ca",
    description="Skywater photonics PDK for the 130nm fab foundry",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("tests",)),
    install_requires=get_install_requires(),
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ],
)

cwd = pathlib.Path(__file__).resolve().parent
_install_to_klayout(
    src=cwd / "sky130ph" / "klayout",
    klayout_subdir_name="macros",
    package_name="sky130ph",
)
