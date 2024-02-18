from setuptools import find_packages, setup


setup(
    name="secondlib",
    version="0.0.11",
    description="An id generator that generated various types and lengths ids",
    package_dir={"": "second_library"},
    packages=find_packages(where="second_library"),
    author="GGEZ",
    author_email="sethukumars774@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
