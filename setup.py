from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()


VERSION = "0.1.0"

DESCRIPTION = "Mim@uf Business Intelligence Library for Portuguese Primary Care"

LONG_DESCRIPTION = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="mimufs",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/DiogoCarapito/mimufs",
    author="Diogo Carapito",
    author_email="diogo.carapito@gmail.com",
    license="Apache License 2.0",
    project_urls={
        "Bug Reports": "https://github.com/DiogoCarapito/mimufs/issues",
        "Source": "https://github.com/DiogoCarapito/mimufs",
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Natural Language :: Portuguese",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    keywords="business intelligence, primary care, data science, medicine",
    python_requires=">=3.7,<3.12",
    install_requires=[
        "pandas>=2.1.3",
        "numpy>=1.26.2",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
)
