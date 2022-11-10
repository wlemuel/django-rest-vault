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
