isort:
	isort ./blockit ./tests

format: isort
	black .
