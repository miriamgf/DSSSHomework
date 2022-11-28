from setuptools import setup, find_packages

setup(
    name='Myrepo',
    version='1.0.0',
    url='https://github.com/miriamgf/DSSSHomework.git',
    author='Miriam Gutiérrez',
    author_email='miriam.gf16@gmail.com',
    description='Example repo',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1', 'turtle==0.0.1' ],
)

