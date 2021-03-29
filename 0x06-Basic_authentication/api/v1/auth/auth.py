#!/usr/bin/env python3
""" Authorization
"""
from flask import request
from typing import List, TypeVar
import sys


class Auth:
    """Template for all authentication system
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require authorization
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path in excluded_paths:
            return False

        if 'path=/api/v1/status' in excluded_paths and 'path=/api/v1/status/' in excluded_paths:
            return False
        
        if path not in excluded_paths:
            return True

    def authorization_header(self, request=None) -> str:
        """Authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user
        """
        return None
