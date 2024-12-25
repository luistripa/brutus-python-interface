from setuptools import setup, find_packages

setup(
    name='brutus',
    version='0.1',
    packages=find_packages(),
    package_data={'brutus': ['lib/*']},
    install_requires=[
        'numpy',
        'pandas',
    ],
)
