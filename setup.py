"""expreccs: A framework to simulate regional and site reservoirs for CO2 storage """

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf8") as file:
    long_description = file.read()

with open("requirements.txt", "r", encoding="utf8") as file:
    install_requires = file.read().splitlines()

with open("dev-requirements.txt", "r", encoding="utf8") as file:
    dev_requires = file.read().splitlines()

setup(
    name="expreccs",
    version="0.2.0",
    install_requires=install_requires,
    extras_require={"dev": dev_requires},
    setup_requires=["setuptools_scm"],
    description="A framework to simulate regional and site reservoirs for CO2 storage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dmar/expreccs",
    author="David Landa-Marbán",
    mantainer="David Landa-Marbán",
    mantainer_email="dmar@norceresearch.no",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords="aquifer co2 opm regional site",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    license="GPL-3.0",
    python_requires=">=3.8, <3.11",
    entry_points={
        "console_scripts": [
            "expreccs=expreccs.core.expreccs:main",
        ]
    },
    include_package_data=True,
)
