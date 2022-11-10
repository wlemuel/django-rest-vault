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

Also add settings for `VAULT` to your project `settings.py`

```
VAULT = {
  'SECRET_KEY': b'.R%@8Xx*q->Gr1dL"-*xm5m,?2Zwcv-y',
  'HTTP_CONTENT_TYPE': 'application/vault-v1',
  'HTTP_ACCEPT': 'application/vault-v1',
  'HTTP_FORMAT': 'vault',
}
```
