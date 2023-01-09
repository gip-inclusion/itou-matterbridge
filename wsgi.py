from app.main import application

# Run it locally with the following command:
# uwsgi --http 127.0.0.1:8000 --master -p 4 -w wsgi:app
app = application
