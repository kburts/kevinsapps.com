FROM python:3.6.0
ENV PYTHONUNBUFFERED 1

RUN echo "bust cache <increment me>" && mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input

CMD sleep infinity