install:
	@python manage.py create_db
	@python manage.py load_db
	@pip install -r requirements.txt
	@npm install -g corsproxy

test:
	@python manage.py test

create:
	@python manage.py create_db

drop:
	@python manage.py drop_db

recreate:
	@python manage.py recreate_db

load_data:
	@python manage.py load_db

run:
	@python site/server.py & python manage.py runserver & corsproxy

stop:
	@kill -9 $(lsof -ti tcp:8000) & kill -9 $(lsof -ti tcp:5000) & kill -9 $(lsof -ti tcp:1337)

clean:
	@find . -name "*.pyc" -print0 | xargs -0 rm -rf
