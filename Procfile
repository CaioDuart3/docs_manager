web: cd docs_manager && python manage.py migrate && python manage.py collectstatic --noinput && gunicorn docs_manager.wsgi --bind 0.0.0.0:$PORT --workers 4
