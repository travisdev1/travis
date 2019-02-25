fedora-happiness-packets
========================

[![Documentation Status](https://readthedocs.org/projects/fedora-happiness-packets/badge/?version=latest)](https://fedora-happiness-packets.readthedocs.io/?badge=latest)

Fedora Account System authentication support and fedora-messaging integration to [Happiness Packets](https://happinesspackets.io) ([demo](https://happinesspackets.fedorainfracloud.org/))


## Documentation

For more help, read the [project documentation](https://fedora-happiness-packets.readthedocs.io/):

[**fedora-happiness-packets.readthedocs.io**](https://fedora-happiness-packets.readthedocs.io/)


## Contributing guidelines

See [CONTRIBUTING.md](https://pagure.io/fedora-commops/fedora-happiness-packets/blob/master/f/.project-docs/CONTRIBUTING.md) for project guidelines.


## Getting started

These instructions run an instance of fedora-happiness-packets on your local machine for development and testing purposes.

### Create development environment

See [setup instructions](https://fedora-happiness-packets.readthedocs.io/setup/development/) in our documentation.

### Testing

The `t` command is a short script to run tests with the correct settings.
It creates a report on test coverage.
While Docker is running, run this command in another window:

```sh
docker-compose exec web sh
./t
```

To run integration tests:

```sh
./manage.py test -v 2 -p integration_test*.py --settings=happinesspackets.settings.testing
```


## Legal

This project is licensed under the [Apache License](https://pagure.io/fedora-commops/fedora-happiness-packets/blob/master/f/LICENSE).
