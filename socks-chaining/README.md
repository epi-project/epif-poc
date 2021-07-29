# SOCKS chaining

## Setup

```shell
$ docker-compose up -d
$ pipenv install click socksx
$ pipenv shell
```

## Run
Allowed:

```shell
$ ./socksx/socksx-py/examples/client.py --destination 172.16.238.6:12345
```

Denied:

```shell
$ ./socksx/socksx-py/examples/client.py --destination 172.16.238.6:54321
```

