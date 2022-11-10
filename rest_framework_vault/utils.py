#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#==============================================================================
#     FileName: utils.py
#      License: MIT
#   LastChange: 9/29/2022 10:06
#    CreatedAt: 9/29/2022 10:06
#==============================================================================
"""
from typing import AnyStr
from base64 import b64encode, b64decode
from Crypto.Cipher import Salsa20

from django.conf import settings
from rest_framework.authentication import get_authorization_header

VAULT_SETTINGS = getattr(settings, "REST_VAULT", {})
VAULT_KEY = VAULT_SETTINGS.get("SECRET_KEY", b"*Thirty-two byte (256 bits) key*")
VAULT_HTTP_CONTENT_TYPE = VAULT_SETTINGS.get("HTTP_CONTENT_TYPE", "application/vault")
VAULT_HTTP_ACCEPT = VAULT_SETTINGS.get("HTTP_ACCEPT", "application/vault")
VAULT_HTTP_FORMAT = VAULT_SETTINGS.get("HTTP_FORMAT", "vault")
VAULT_USE_TOKEN_AS_KEY = VAULT_SETTINGS.get("USE_TOKEN_AS_KEY", True)
# VAULT_ALGORITHM = VAULT_SETTINGS.get('ALGORITHM', 'salsa20')

if isinstance(VAULT_KEY, str):
    VAULT_KEY = VAULT_KEY.encode()


def get_key(request) -> bytes:
    if request is None:
        return VAULT_KEY

    auth = get_authorization_header(request).split()

    if not auth or len(auth) != 2:
        return VAULT_KEY

    try:
        token = auth[1].decode()
    except UnicodeError:
        return VAULT_KEY

    if len(token) < 32:
        return VAULT_KEY

    return token[31::-1].encode()


def encrypt(data: bytes, key: bytes = VAULT_KEY) -> bytes:
    """
    Encrypt data with algorithms Salsa20 & Base64.

    :param key: secret key
    :param data: plain text
    :return: encrypted data
    """
    if data is None:
        return bytes()

    cipher = Salsa20.new(key=key)
    encrypted_data = cipher.nonce + cipher.encrypt(data)
    return b64encode(encrypted_data)


def decrypt(data: AnyStr, key: bytes = VAULT_KEY) -> bytes:
    """
    Decrypt data with algorithms Salsa20 & Base64.

    :param key: secret key
    :param data: encrypted data
    :return: plain text
    """
    if data is None:
        return bytes()

    encrypted_data = b64decode(data)
    nonce = encrypted_data[:8]
    cipher_text = encrypted_data[8:]
    cipher = Salsa20.new(key=key, nonce=nonce)

    return cipher.decrypt(cipher_text)
