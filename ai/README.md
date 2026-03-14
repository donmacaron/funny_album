# Local dev quickstart

1. python -m venv .venv
2. source .venv/bin/activate
3. pip install -r backend/requirements.txt
4. cd backend && python manage.py migrate
5. python manage.py createsuperuser
6. python manage.py runserver
