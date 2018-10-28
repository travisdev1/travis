FROM python:2-alpine

#Install required system packages
RUN apk add --update --no-cache build-base bash readline libffi-dev ncurses-dev python2-dev postgresql-dev

# Install required Python packages
COPY ./requirements /requirements
RUN pip install -r /requirements/dev.txt

# Set correct DJANGO_SETTINGS_MODULE
ENV DJANGO_SETTINGS_MODULE=happinesspackets.settings.dev

# Copy project files into container
COPY . /


# Check if client_secrets.json is present, and generate if not
RUN apk add --update --no-cache curl
RUN chmod +x generate_client_secrets.sh
RUN ./generate_client_secrets.sh

RUN ./manage.py collectstatic --noinput

# Expose Django port
EXPOSE 8000 

