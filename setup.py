from setuptools import setup

setup(
    name='snake_gym',
    version='1.7',
    author="Vivek Verma",
    packages=["snake_gym"],
    author_email="vivnps.verma@gmail.com",
    url="https://github.com/vivek3141/snake-ai",
    license='MIT',
    description="Gym environment for Snake",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
