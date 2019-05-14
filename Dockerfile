FROM python:3.5.2
EXPOSE 8000
RUN mkdir /usr/src/app
RUN mkdir /usr/src/app/logs
RUN mkdir /usr/src/app/static
RUN mkdir /usr/src/app/staticfiles
COPY req.txt /usr/src/app/req.txt

WORKDIR /usr/src/app/python
RUN pip install -r /usr/src/app/req.txt

WORKDIR /usr/src/app/
CMD [ "python", "manage.py", "collectstatic", "-v0", "--noinput" ]
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]