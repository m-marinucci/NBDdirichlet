from setuptools import setup, find_packages

setup(
    name='nbddirichlet',
    version='0.1.0',
    description='NBD-Dirichlet Model of Consumer Buying Behavior for Marketing Research',
    author='Massimiliano Marinucci',
    author_email='mmarinucci@numinate.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'pandas',
    ],
)