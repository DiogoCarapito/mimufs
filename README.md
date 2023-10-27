# mimufs
Mim@uf Business Intelligence Library for Portuguese Primary Care

## Cheatsheet


### Build and upload to PyPI

setup.py to build
```bash
python3 setup.py sdist bdist_wheel
```

twine to upload to PyPI
```bash
twine check dist/*
twine upload dist/*
```
