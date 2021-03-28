#!/usr/bin/env python3
""" Authorization
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Template for all authentication system
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require authorization
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user
        """
        return None
