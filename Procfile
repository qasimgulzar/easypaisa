release: python manage.py migrate

web: mkdir static; python collectstatic --no-input; gunicorn easypaisa.wsgi -b 0.0.0.0:$PORT
