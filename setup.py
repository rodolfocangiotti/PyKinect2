from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="pykinect2",
    version="0.2.0",
    description="Wrapper to expose Kinect for Windows v2 API in Python",
    license="MIT",
    author="Rodolfo Cangiotti",
    author_email="hello@rodolfocangiotti.art",
    url="https://github.com/rodolfocangiotti/PyKinect2/",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
    ],
    packages=find_packages(),
    install_requires=requirements,
)
