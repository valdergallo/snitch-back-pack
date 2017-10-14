# snitch-back-pack

Snitch Backend with DRF to manager the users e access in urls. 
This project is created with `Python 3.6` and `Django`.
Im using `Token` authentication with `Django Rest Framework`

### how I get one token to connect

Send one POST to 

```
    >>> curl -X POST "username=batman&password=topsecret" http://127.0.0.1:8000/api/api-token/
    >>> {id: 1, token: 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b}
```

TO use your token 

```
    >>> curl -X GET http://127.0.0.1:8000/api/example/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
```

#### Nice commands to get one Token for developers

| command          |  description                          |
|------------------|---------------------------------------|
| drf_create_token | create your token without POST em API |
| runserver        | run developer server                  |
| shell            | run python prompt                     |

### to start a developer

Using virtualenv
```
    >>> ptyhon virtualenv --python=python3.6 .env
    >>> source .env/bin/activate
    >>> pip install -r requirements.txt
```
