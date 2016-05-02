install:
	@pip install -r requirements.txt

run:
	@python manage.py runserver 0:8000

clean:
	@find . -name "*.pyc" -print0 | xargs -0 rm -rf

