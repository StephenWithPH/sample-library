from setuptools import setup, find_packages

setup(
    name='samplelibrary',
    version='0.0.1',
    description='a silly thing to exercise what might be a bug',
    packages=find_packages(exclude=['*tests*']),
    install_requires=[
        'protobuf>=3.5.2',
    ],
)
