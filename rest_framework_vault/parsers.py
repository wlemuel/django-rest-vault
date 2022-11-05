#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#==============================================================================
#     FileName: parsers.py
#      License: MIT
#   LastChange: 9/29/2022 09:58
#    CreatedAt: 9/29/2022 09:58
#==============================================================================
"""
import codecs

from django.conf import settings
from rest_framework.parsers import BaseParser
from rest_framework.exceptions import ParseError
from rest_framework.settings import api_settings
from rest_framework.utils import json

from .renderers import VaultRenderer
from .utils import decrypt, get_key, VAULT_HTTP_CONTENT_TYPE, VAULT_USE_TOKEN_AS_KEY


class VaultParser(BaseParser):
    """
    Parses Vault-serialized data.
    """

    media_type = VAULT_HTTP_CONTENT_TYPE
    renderer_class = VaultRenderer
    strict = api_settings.STRICT_JSON

    def parse(self, stream, media_type=None, parser_context=None):
        parser_context = parser_context or {}
        encoding = parser_context.get("encoding", settings.DEFAULT_CHARSET)

        try:
            decoded_stream = codecs.getreader(encoding)(stream)

            if VAULT_USE_TOKEN_AS_KEY:
                request = parser_context.get("request", None)
                key = get_key(request)
                data = decrypt(decoded_stream.read(), key)
            else:
                data = decrypt(decoded_stream.read())

            parse_constant = json.strict_constant if self.strict else None
            return json.loads(data, parse_constant=parse_constant)
        except ValueError as exc:
            raise ParseError("Data parse error - %s" % str(exc))
