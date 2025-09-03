install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	pytest -vv --cov=src tests/test_*.py

format:
	black src/ src/*.py

lint:
	pylint --disable=R,C src/*.py src/utils/*.py src/ui/*.py src/pages/*.py src/autogui/*.py tests/*.py

#container-lint:
#	docker run -rm -i hadolint/hadolint < Dockerfile

refactor:
	format lint

deploy:
	echo "deploy not implemented"

all: install lint test format