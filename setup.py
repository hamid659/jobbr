from setuptools import setup, find_packages

setup(
    name="jobbr",
    version="1.0.0",
    description="A CLI tool to manage jobs and queues via Jobbr API",
    author="Hamid H",
    author_email="hamid2160659@gmail.com",
    url="https://github.com/hamid659/jobbr.git", 
    packages=find_packages(),
    install_requires=[
        "click>=8.1.3",
        "requests>=2.31.0",
        "tenacity>=8.2.2",
    ],
    entry_points={
        "console_scripts": [
            "jobbr=jobbr.cli:cli",  # Links the CLI tool to the main function in cli.py
        ],
    },
    python_requires=">=3.8",
    keywords="jobs queues API CLI",
)
