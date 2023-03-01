install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=stackquestions --cov=soflogic test_stackoverflow.py

lint:
	pylint --disable=R,C *.py soflogic/*.py main.py

format:
	black *.py soflogic 

all: install lint test format