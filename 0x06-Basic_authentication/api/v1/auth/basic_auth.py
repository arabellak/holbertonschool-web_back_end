#!/usr/bin/env python3
"""
Manage the API authentication.
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """Inherits from Auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extract"""
        if authorization_header is None:
            return None

        if type(authorization_header) != str:
            return None

        if authorization_header[:6] == 'Basic ':
            return authorization_header[6:]
        else:
            return None

    def decode_base64_authorization_header(
                                            self,
                                            base64_authorization_header: str
                                            ) -> str:
        """Decoded value of a Base64 string"""
        if base64_authorization_header is None:
            return None

        if type(base64_authorization_header) is not str:
            return None

        try:
            return b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
                                  self,
                                  decoded_base64_authorization_header: str
                                  ) -> (str, str):
        """Return
            - User email and password
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if type(decoded_base64_authorization_header) is not str:
            return None, None

        if ':' in decoded_base64_authorization_header:
            uno = decoded_base64_authorization_header.split(sep=':')
            return tuple(uno)
        else:
            return None, None

    def user_object_from_credentials(
                                      self,
                                      user_email: str,
                                      user_pwd: str
                                      ) -> TypeVar('User'):
        """Return
            - User instance based on his email and password.
        """
        if user_email is None or type(user_email) != str:
            return None

        if user_pwd is None or type(user_pwd) != str:
            return None

        pe = User.search({'email': user_email})
        if not pe:
            return None

        for pe_pe in pe:
            if pe_pe.is_valid_password(user_pwd):
                return pe_pe
        return None
