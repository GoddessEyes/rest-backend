lint:
	black --config .pyproject.toml --skip-string-normalization src
	isort -y
	flake8 --config=.flake8
	pylint src
