rom setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=3.10"]
setup(
    name="snowflakes",
    version="0.0.1",
    author="Miriam Gutiérrez",
    author_email="miriam.gf16@gmail.com",
    description="Example of Github Repository",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/miriamgf/DSSSHomework.git",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",

    ],
)