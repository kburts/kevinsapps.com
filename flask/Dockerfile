FROM python:3.4
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=True

RUN echo "bust cache <increment me>" && mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt

CMD sleep infinity