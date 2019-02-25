fedora-happiness-packets
========================

[![Documentation Status](https://readthedocs.org/projects/fedora-happiness-packets/badge/?version=latest)](https://fedora-happiness-packets.readthedocs.io/?badge=latest)

Fedora Account System authentication support and fedora-messaging integration to [Happiness Packets](https://happinesspackets.io) ([demo](https://happinesspackets.fedorainfracloud.org/))


## Documentation

For more help, read the [project documentation](https://fedora-happiness-packets.readthedocs.io/):

[**fedora-happiness-packets.readthedocs.io**](https://fedora-happiness-packets.readthedocs.io/)


## Contributing guidelines

See [CONTRIBUTING.md](https://pagure.io/fedora-commops/fedora-happiness-packets/blob/master/f/.project-docs/CONTRIBUTING.md) for project guidelines.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You require the following things for the software to be installed.

- Docker
- Docker-Compose
- Python (Version 3 is recommended)

## Installing

Clone the repository:

```
git clone https://pagure.io/fedora-commops/fedora-happiness-packets.git
```

Change the working directory to fedora-happiness-packets

```
cd fedora-happiness-packets
```

In order for the login and send views to work, you must supply an OpenID Connect Client ID and Client Secret:

```
chmod +x generate_client_secrets.sh
./generate_client_secrets.sh
```

## Running

To run on http://localhost:8000/ :
```
docker-compose up
```
After making any changes to the code, make sure to rebuild the container:
```
docker-compose up --build
```
## Testing

The `t` command is a very short shell script that runs the tests with the correct settings and reports on coverage.
While the docker is up, in another shell run :
```
docker-compose exec web sh
./t
```
To run the integration tests::
```
./manage.py test -v 2 -p integration_test*.py --settings=happinesspackets.settings.tsting
```
### License

This project is licensed under the Apache License - see LICENSE in files.
