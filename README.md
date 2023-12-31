[![CD/CI](https://github.com/DiogoCarapito/mimufs/actions/workflows/cdci.yaml/badge.svg)](https://github.com/DiogoCarapito/mimufs/actions/workflows/cdci.yaml)
![PyPI Latest Release](https://img.shields.io/pypi/v/mimufs.svg)

# mimufs

**mimufs** is a python library with tools for data processing and analysis in **Portuguese Prymary Health Care**.
It has a set of functions to facilitate data processing from *MIM@UF* and *BI-CSP* plataforms. It also has a set of functions to facilitate data analysis and visualization.

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
