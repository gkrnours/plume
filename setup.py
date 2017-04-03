from setuptools import setup, find_packages

setup(
    name="plume",
    version="0.0.1",
    description="A web application to manage a pelican website",
    long_description="",
    url="https://github.com/gkrnours/plume",
    author="gkr",
    author_email="couesl@gmail.com",
    license="MIT",
    classifiers=[
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Intended Audience :: End Users/Desktop",
    "Topic :: Software Development",
    "Environment :: Internet :: WWW/HTTP :: Site Management",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "flask",
        "markdown",
        "peewee",
        "pelican",
        "pelican-sqlgenerator",
        "python-slugify",
        "wtf-peewee",
        "wtforms",
    ],
    dependency_links = [
            "https://github.com/gkrnours/pelican-sqlgenerator/tarball/master#egg=pelican-sqlgenerator-0.0.1'",
    ],
    entry_points="""
        [console_scripts]
        plume=plume.server:main
    """,
)
