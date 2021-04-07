#!/usr/bin/env python3
"""
Manage the API authentication.
"""
from api.v1.auth.auth import Auth
from flask import request
import uuid
from models.user import User


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
            sessionId = str(uuid.uuid4())
            self.user_id_by_session_id[sessionId] = user_id
            return sessionId

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Return
             - ID based on a Session ID
        """
        if session_id is None or type(session_id) is not str:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Return
            - User instance on a cookie value
        """
        user_cookie = self.session_cookie(request)
        if user_cookie is None:
            return None

        d = self.user_id_for_session_id(user_cookie)
        return User.get(d)
