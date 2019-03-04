===================================================
 Setting up a development environment on Windows
===================================================

This guide will take you through the process to setup your development environment on Windows OS.

Prerequisites
===============

You will need the following programs installed on your system before proceeding with the setup.

#. `Git <https://git-scm.com/>`_
#. `Python <https://www.python.org/downloads/>`_ (version >= 3.5)
#. `Docker Desktop for Windows <https://hub.docker.com/editions/community/docker-ce-desktop-windows>`_ (Download, installation, and run instructions available)
#. Docker Compose (Docker Compose is included as part of Docker Desktop, but if you still need to download it, you can do it from `here <https://docs.docker.com/compose/install/>`_)


Setting up the development environment
========================================

#. Fork the `current repository <https://pagure.io/fedora-commops/fedora-happiness-packets>`_ to your profile.
#. Clone this forked repository (ssh method is recommended, the steps can be found `here <https://docs.pagure.org/pagure/usage/first_steps.html>`_) to your system using Git with the following command::

    git clone "https://pagure.io/forks/<user_name>/fedora-commops/fedora-happiness-packets.git"

    OR, if using ssh,

    git clone "ssh://git@pagure.io/forks/<user_name>/fedora-commops/fedora-happiness-packets.git"

#. Once cloned, move inside the directory using the command::

    cd fedora-happiness-packets

#. Start the Docker application(With elevated/admin access).
#. Run the client secret generation script::

    chmod +x generate_client_secrets.sh
    generate_client_secrets.sh

    Here, you might get an error saying::

    /bin/sh: ./generate_client_secrets.sh: not found

    This occurs mostly due to line endings being CRLF instead or the required LF.
    This can be changed by modifying the settings of your respective editor, or else from console using `this method <https://github.com/postlight/headless-wp-starter/issues/171#issuecomment-451682572>`_

#. To run the web server, run::

    docker-compose up

Once executed successfully, you should be able to view the main page on `http://localhost:8000/ <http://localhost:8000/>`_

Congratulations, you have successfully setup the development environment on your system.

After making changes to any file, you'll have to run the command::

    docker-compose up --build

For ``docker-compose up`` or ``docker-compose up --build`` you might get an error of::

    alpinelinux.org error ERROR: unsatisfiable constraints

This can be resolved by simply following the below steps

#. Open Docker settings.
#. Click on Network.
#. Look for 'DNS Server' section.
#. It is set to *Automatic* by default, change it to *fixed*.
#. The IP address should now be editable. Change it from ``8.8.8.8`` to ``8.8.4.4``.
#. Save the settings and restart Docker.

In order to run tests, make sure to execute ``docker-compose up`` command. Now in a new terminal(for the same container) run::

    docker-compose exec web sh

Then the terminal will show a ``#`` symbol.
Simply type in ``./t`` (or ``t``) to initiate the test suite.

(The test suite are run by running the ``./t`` script, which runs the tests with the appropriate testing settings and provides a coverage report.)

Integration tests are run via the following command::

    docker-compose exec web ./manage.py test -v 2 -p integration_test*.py --settings=happinesspackets.settings.tsting

If a ``file not found`` error occurs, try removing the ``./`` from the command and try again.
