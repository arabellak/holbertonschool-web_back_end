#!/usr/bin/env python3
"""
Manage the API authentication.
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Auth require
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != '/':
            path += '/'

        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """Auth header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """User
        """
        return None
