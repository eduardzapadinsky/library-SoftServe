FROM python:3.10

#ENV PYTHONDONTWRITECODE 1
#ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/om54

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/om54

#EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]