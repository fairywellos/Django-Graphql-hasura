FROM python:3.7.2

ENV PYTHONUNBUFFERED 1
WORKDIR /code

# Run this first so the first image layer is cached
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN python manage.py migrate_schemas --shared

ADD ./ /code/
RUN echo "test"
