[![Release](https://github.com/DiogoCarapito/mimufs/actions/workflows/release.yaml/badge.svg)](https://github.com/DiogoCarapito/mimufs/actions/workflows/release.yaml)

# Mimufs

Mimufs is a python library with tools for data processing and analysis in Portuguese Prymary Health Care.
It has a set of functions to facilitate data processing from MIM@UF and BI-CSP plataforms. It also has a set of functions to facilitate data analysis and visualization.

## Installation
To install mimufs, run this command in your project's terminal:
```bash
pip install mimufs
```
or in your jupyter notebook:
```python
!pip install mimufs
```

## Usage
mimufs can be used in python scripts or in jupyter notebooks.
```python
import mimufs as mm
```
for specific data processing functions:
```python
from mimufs import processing
```

for specific data analysis functions:
```python
from mimufs import analysis
```

for specific visualization functions:
```python
from mimufs import visualization
```


## Cheatsheet
### venv
create venv
```bash
python3 -m venv .venv
```
activate venv
```bash
source .venv/bin/activate
```

### Build package and upload to PyPI
```bash
python3 setup.py sdist bdist_wheel
twine check dist/*
twine upload dist/*
```