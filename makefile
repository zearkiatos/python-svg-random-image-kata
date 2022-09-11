docker-up:
	docker compose up --build -d
	docker exec -it python-svg-random-image-kata python imageGenerator.py

docker-down:
	docker compose down