from setuptools import setup

setup(
    name="application_Flask_blog",
    version="0.1.0",
    packages=['application-blog'],
    author="th",
    install_requires=["flask","flask-pymongo","dynaconf"]
)