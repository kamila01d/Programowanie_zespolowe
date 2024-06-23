START:
	ENV_FILE="config/local"

poetry-install:
	poetry install --no-root


poetry-update:
	poetry update


lint:
	black . && isort .


run:
	uvicorn src.main:app --reload