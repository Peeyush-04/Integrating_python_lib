from setuptools import find_packages, setup


setup(
    name="integratedlib",
    version="0.0.16",
    description="An id generator that generated various types and lengths ids",
    package_dir={"": "integrator"},
    packages=find_packages(where="integrator"),
    author="GGEZ",
    author_email="sethukumars774@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
