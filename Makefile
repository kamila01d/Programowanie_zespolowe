poetry-install:
	poetry install --no-root


poetry-update:
	poetry update


lint:
	black . && isort .