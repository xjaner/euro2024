FROM python:3

RUN apt-get update && \
    apt-get install -y  && \
    apt-get install -y gettext
#gettext
# RUN apt-get update && \
#     apt-get install -y && \
#     pip install --upgrade pip && \
#     pip3 install uwsgi

ENV DJANGO_ENV=dev
# ENV DJANGO_ENV=prod
ENV DOCKER_CONTAINER=1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000
EXPOSE 8001

# Will also be done in docker-compose
COPY ./euro2024 /opt/euro2024
RUN pip install -r /opt/euro2024/requirements.txt

# Temporarily disabled
# CMD ["uwsgi", "--ini", "/opt/euro2024/uwsgi.ini"]
