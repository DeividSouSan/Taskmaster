run:
	docker compose --file src/infra/compose.yaml up -d && \
	python wsgi.py

stop:
	docker compose --file src/infra/compose.yaml down
