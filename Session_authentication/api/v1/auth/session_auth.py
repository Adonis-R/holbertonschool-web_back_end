#!/usr/bin/env python3
"""Module for basic authentication using Flask."""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """
    Session authentication class that extends the Auth class.
    """
    user_id_by_session_id = {}  # New class attribute

    def __init__(self):
        """Initialize SessionAuth."""
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session ID for a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            str: The session ID.
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())  # Generate session ID like id in Base
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Retrieves the user ID associated with a session ID.

        Args:
            session_id (str): The session ID.

        Returns:
            str: The user ID associated with the session ID.
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None):
        """
        Retrieves the current user based on the session ID.

        Args:
            request: The Flask request object.

        Returns:
            returns a User instance based on a cookie value.
        """
        if request is None:
            return None
        session_id = self.session_cookie(request)
        if session_id is None:
            return None
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        return User.get(user_id)

    def destroy_session(self, request=None):
        """
        Destroys the session for the current user.

        Args:
            request: The Flask request object.

        Returns:
            bool: True if the session was successfully destroyed, False otherwise.
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_id]
        return True
