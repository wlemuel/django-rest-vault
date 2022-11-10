# django-rest-vault

Api data decryption and encryption support for Django REST Framework

## Requirements

- Python (3.6+)
- Django (2.2.16+)
- Django REST Framework (3.10.3+)

## Installation

Install using `pip`

```sh
pip install django-rest-vault
```

## Usage

Add `rest_framework_vault` to `INSTALLED_APPS` and `REST_FRAMEWORK`

```
INSTALLED_APPS = (
  ...
  'rest_framework',       # Django REST Framework
  'rest_framework_vault', # Django REST Vault
  ...
)

REST_FRAMEWORK = {
  'DEFAULT_PARSER_CLASSES': (
    'rest_framework.parsers.JSONParser',
    'rest_framework_vault.parsers.VaultParser',
  ),
  'DEFAULT_RENDERER_CLASSES': (
    'rest_framework.renderers.JSONRenderer',
    'rest_framework_vault.renderers.VaultRenderer',
  ),
}
```

Also add settings for `REST_VAULT` to your project `settings.py`

```
REST_VAULT = {
  'SECRET_KEY': b'*Thirty-two byte (256 bits) key*',
  'HTTP_CONTENT_TYPE': 'application/vault',
  'HTTP_ACCEPT': 'application/vault',
  'HTTP_FORMAT': 'vault',
  'USE_TOKEN_AS_KEY': True,
}
```

## Examples

### Get Users List (Default - json)

```sh
curl -u admin:123456 'http://localhost:8000/users/'
```
```
{"count":1,"next":null,"previous":null,"results":[{"url":"http://localhost:8000/users/1/","username":"admin","email":"admin@example.com","groups":[]}]}
```

### Get Users List (vault)

```sh
curl -u admin:123456 'http://localhost:8000/users/?format=vault
```
```
6ARyPVxylOavaXFslb/Ab/AiYWsoFqCIu8pJ9bhnGI9zozmRkdWOySt4bI7CY0detuA9RkWhnHMS4/gLIu907E0Z8A0vHP56z493Zkld+UYSS94nk19LDr5TfkOEAQ0+A4C1AgbxlgSWk2XpxpDVZc4Nwm9rXOrP1xpIWXwAUREG520mdPwiR8AYPUpRVExsH7hSKXiasEVczAxPsXVKaamv/WC3CxgMldrIRA==
```
