from setuptools import setup, find_packages
from codecs import open
from os import path

import l2m

here = path.abspath(path.dirname(__file__))

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='l2m',
    version=l2m.__version__,
    description='L2M: Practical posterior Laplace approximation with optimization-driven second moment estimation.',
    url='https://github.com/ml-poa/l2m',
    author='Machine Learning Porto Alegre',
    author_email='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(exclude=[]),
    install_requires=requirements
)