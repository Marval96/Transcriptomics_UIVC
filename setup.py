from setuptools import setup, find_packages

setup(
    name="hubs_finder",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
    ],
    entry_points={
        "console_scripts": [
            "hubs-finder=hubs_finder.cli:main",
        ],
    },
)
