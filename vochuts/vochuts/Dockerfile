FROM python:3.6.0
ENV PYTHONUNBUFFERED 1

RUN echo "bust cache <increment me>" && mkdir /voccode
WORKDIR /voccode
ADD requirements.txt /voccode/
RUN pip install -r requirements.txt

CMD python manage.py collectstatic --no-input
CMD python manage.py migrate

CMD sleep infinity