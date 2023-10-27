"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()


VERSION = "0.0.1"
DESCRIPTION = "Mim@uf Business Intelligence Library for Portuguese Primary Care"
LONG_DESCRIPTION = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="mimufs",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/DiogoCarapito/mimufs",
    author="DiogoCarapito",
    author_email="diogo.carapito@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: Apache License 2.0",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="business intelligence, primary care, data science, medicine",
    packages=find_packages(where="mimufs"),
    python_requires=">=3.7, <4",
    install_requires=["pandas"],
    project_urls={
        "Bug Reports": "https://github.com/DiogoCarapito/mimufs/issues",
        "Source": "https://github.com/DiogoCarapito/mimufs",
    },
)
