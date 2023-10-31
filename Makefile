install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	pytest -vv --cov=src tests/test_*.py

format:
	black . *.py

add:
	git add .

lint:
	pylint --disable=R,C *.py 

all: install lint test format
