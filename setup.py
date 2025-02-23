from setuptools import setup, find_packages

# Install package using `pip install -e .`

setup(
    name="sort",
    version="0.1.0",
    packages=find_packages(),
    description="A package for sorting algorithms",
    author="Rett Graham",
    author_email="rettg@umich.edu",
    url="https://github.com/rettag/sorting-algorithms",
    install_requires=[
        "numpy",
        "matplotlib",
    ],
    license="MIT",
)
