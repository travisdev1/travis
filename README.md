# Fedora-Happiness-Packets

Fedora-Happiness-Packets contains the codebase for fedora hosted version of [happinesspacks.io](https://happinesspackets.io) to be used during appreciation week. The live service is hosted [here](http://happinesspackets.fedorainfracloud.org).

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
