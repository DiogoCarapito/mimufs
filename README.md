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

### medico()

```python
import pandas as pd
from mimufs.processing import medico

df = medico(df, column="Médico Familia")

```

