from setuptools import setup

setup(
    name="application_test",
    version="0.1.0",
    packages=['application'],
    author="th",
    install_requires=["flask","flask-pymongo","dynaconf"]
)