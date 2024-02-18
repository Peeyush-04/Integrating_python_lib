from setuptools import find_packages, setup


setup(
    name="firstlib",
    version="0.0.2",
    description="An id generator that generated various types and lengths ids",
    package_dir={"": "first_library"},
    packages=find_packages(where="first_library"),
    author="GGEZ",
    author_email="sethukumars774@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
