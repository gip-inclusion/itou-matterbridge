from app.main import application

# uwsgi --http 127.0.0.1:8000 --master -p 4 -w wsgi:app
# Clever: CC_PYTHON_MODULE="wsgi:app"
app = application
