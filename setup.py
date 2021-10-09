from setuptools import find_packages, setup

with open("README.md") as f:
    desc = f.read()

extras = {
    "dev": [
        "pytest<5.4",
        "pytest-asyncio<0.11.0",
        "pytest-cov",
        "pre-commit"
    ],
}

install_requires = []

setup(
    name="stac-sqlalchemy",
    description="Another SQLAlchemy backend for stac-fastapi.",
    long_description=desc,
    long_description_content_type="text/markdown",
    version="0.1.0",
    author=u"Jeff Albrecht",
    author_email="geospatialjeff@gmail.com",
    url="https://github.com/geospatial-jeff/stac-sqlalchemy",
    license="apache",
    python_requires=">=3.9",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="stac sqlalchemy stac-fastapi",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=install_requires,
    test_suite="tests",
    extras_require=extras,
    tests_require=extras["dev"],
)