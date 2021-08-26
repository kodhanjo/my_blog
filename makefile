migrate:
	python3.8 manage.py db migrate -m "Migration"
	python3.8 manage.py db upgrade