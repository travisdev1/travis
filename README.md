# fedora-happiness-packets

This project contains the codebase for fedora hosted version of happinesspackets.io to be used during Appreciation week.

# Setup

To run this project or the tests, you need to set up a virtualenv, install the dev requirements and set
the correct ``DJANGO_SETTINGS_MODULE``, for example with::

    virtualenv --no-site-packages --prompt='(happinesspackets)' virtualenv/
    source virtualenv/bin/activate
    pip install -r requirements/dev.txt
    export DJANGO_SETTINGS_MODULE=happinesspackets.settings.dev
    ./manage.py collectstatic
    python manage.py migrate
    ./t

To run on http://127.0.0.1:8000/ :

    python manage.py runserver

Don't forget to start the mail server:

    python -m smtpd -n -c DebuggingServer localhost:2525

The ``t`` command is a very short shell script that runs the tests with the correct settings and reports on coverage.

To run the integration tests::

    ./manage.py test -v 2 -p integration_test*.py --settings=happinesspackets.settings.tsting
