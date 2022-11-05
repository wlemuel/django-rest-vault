#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#==============================================================================
#     FileName: renderers.py
#      License: MIT
#   LastChange: 9/29/2022 09:58
#    CreatedAt: 9/29/2022 09:58
#==============================================================================
"""
from rest_framework.renderers import BaseRenderer, JSONRenderer

from .utils import (
    encrypt,
    get_key,
    VAULT_HTTP_FORMAT,
    VAULT_HTTP_ACCEPT,
    VAULT_USE_TOKEN_AS_KEY,
)


class VaultRenderer(BaseRenderer):
    """
    Renderer which encrypts data.
    """

    media_type = VAULT_HTTP_ACCEPT
    format = VAULT_HTTP_FORMAT
    json_renderer = JSONRenderer()
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Render `data` into encrypted data, returning a bytestring.
        """
        raw_json = self.json_renderer.render(
            data, accepted_media_type, renderer_context
        )
        renderer_context = renderer_context or {}

        if VAULT_USE_TOKEN_AS_KEY and renderer_context:
            request = renderer_context.get("request", None)
            key = get_key(request)
            return encrypt(raw_json, key)

        return encrypt(raw_json)
