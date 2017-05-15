release: python manage.py migrate

web: mkdir static; python manage.py collectstatic --no-input; gunicorn easypaisa.wsgi -b 0.0.0.0:$PORT
