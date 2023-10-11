make start:
	poetry run uvicorn src.main:app --reload

req:
	poetry export --without-hashes --format=requirements.txt > requirements.txt

env:
	cp .env.template .env

lint:
	poetry run ruff .

docker-install: env req
	docker-compose build

docker:
	docker-compose up -d