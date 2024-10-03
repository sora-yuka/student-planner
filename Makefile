# RUNNING PROJECT
r:
	./manage.py runserver

# MAKING MIGRATIONS
m:
	./manage.py makemigrations
	./manage.py migrate

# CREATING SUPER USER
su:
	./manage.py createsuperuser

# RUNNING CELERY
c:
	celery -A config worker -l info