# fedora-happiness-packets

This project contains the codebase for fedora hosted version of happinesspackets.io to be used during Appreciation week. The live service is hosted [here](http://happinesspackets.fedorainfracloud.org)

# Setup

Make sure you have Docker and Docker Compose installed.

In order for the login and send views to work, you must supply an OpenID Connect Client ID and Client Secret:

    oidc-register https://iddev.fedorainfracloud.org/openidc/ http://localhost:8000/oidc/callback/ 

To run on http://localhost:8000/ :

    docker-compose up

After making any changes to the code, make sure to rebuild the container:

    docker-compose up --build


The ``t`` command is a very short shell script that runs the tests with the correct settings and reports on coverage.

To run it:
    
    docker-compose exec web sh
    ./t

To run the integration tests::

    ./manage.py test -v 2 -p integration_test*.py --settings=happinesspackets.settings.tsting
