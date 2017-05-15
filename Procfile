web: python manage.py collectstatic --no-input

web: gunicorn easypaisa.wsgi -b 0.0.0.0:$PORT
