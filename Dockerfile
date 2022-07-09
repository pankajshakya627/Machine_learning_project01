FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPORT $PORT
CMD gunicorn --worker=4 --bind= 0.0.0.0:$PORT --access-logfile app:app