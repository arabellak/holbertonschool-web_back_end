#!/usr/bin/env python3
"""
Manage the API authentication.
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Inherits from Auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Base64"""
        if authorization_header is None:
            return None

        if type(authorization_header) != str:
            return None

        if authorization_header[:6] == 'Basic ':
            return authorization_header[6:]
        else:
            return None
