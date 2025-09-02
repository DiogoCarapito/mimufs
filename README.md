# python_project_template

[![Github Actions Workflow](https://github.com/DiogoCarapito/python_project_template/actions/workflows/main.yaml/badge.svg)](https://github.com/DiogoCarapito/python_project_template/actions/workflows/main.yaml)

Python project template.

Python version: 3.12

## cheat sheet

### setup

copy all files (folders, hidden and non-hidden files) to the higher directory
usefull if you clone the repo into your desired directory
ignore if clone and after change the name of the directory

```bash
mv python_project_template/{*,.*} . && rm -r python_project_template/
```

### venv

create venv

```bash
python3.12 -m venv .venv
```

activate venv

```bash
source .venv/bin/activate
```
