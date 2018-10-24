FROM python:2-alpine

#Install required system packages
RUN apk add --update --no-cache build-base bash readline libffi-dev ncurses-dev openssl-dev

# Install required Python packages
COPY ./requirements /requirements
RUN pip install -r /requirements/dev.txt

# Set correct DJANGO_SETTINGS_MODULE
ENV DJANGO_SETTINGS_MODULE=happinesspackets.settings.dev

# Copy project files into container
COPY . /

RUN ./manage.py collectstatic --noinput
RUN python manage.py migrate

# Expose Django port
EXPOSE 8000 

