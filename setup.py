from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()


VERSION = "0.0.26"

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
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: Apache Software License",
    ],
    keywords="business intelligence, primary care, data science, medicine",
    python_requires=">=3.7,<3.12",
    install_requires=[],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
)
