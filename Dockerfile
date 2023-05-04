FROM public.ecr.aws/docker/library/python:3.11

WORKDIR /app

COPY app.py /app

RUN pip install Flask Flask-SQLAlchemy PyMySQL mysqlclient

EXPOSE 80

CMD ["python3", "app.py"]