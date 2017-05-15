release: python manage.py migrate
web: python collectstatic --no-input

web: gunicorn easypaisa.wsgi -b 0.0.0.0:$PORT
