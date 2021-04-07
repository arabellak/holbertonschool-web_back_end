#!/usr/bin/env python3
"""
Manage the API authentication.
"""
from api.v1.auth.auth import Auth
from flask import request
import uuid


class SessionAuth(Auth):
    """Validates
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates
                - session ID for a user:id
            Return
                -None
        """
        if user_id is None or type(user_id) is not str:
            return None
        else:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
