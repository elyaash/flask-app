# Flask App

## Run app with gunicorn
gunicorn -w 4 -b 0.0.0.0:5500 app:app

## Run app with Flask
flask --app app run --debug
