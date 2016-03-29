clean:
	find . -name "*.pyc" -exec rm -rf {} \;
run: clean
	python manage.py runserver 0.0.0.0:8000
migrate:
	python manage.py migrate
migrations:
	python manage.py makemigrations
install:
	npm install
	bower install
	pip install -r requirements.txt
	make migrate
user:
	python manage.py createsuperuser

shell:
	python manage.py shell

tests: clean
	python manage.py test --settings=default.settings_tests