#!/usr/bin/env python3
"""
Auth module - template for future authentication systems.
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Template class for handling API authentication."""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if a given path requires authentication.

        Arguments:
        path -- the path to check
        excluded_paths -- list of paths that don't require authentication

        Returns:
        False for now (will be implemented later)
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        # Normalize path to ensure it ends with a slash
        normalized_path = path if path.endswith('/') else path + '/'

        for excluded in excluded_paths:
            if excluded == normalized_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.

        Arguments:
        request -- the Flask request object

        Returns:
        None for now (will be implemented later)
        """
        if request is None:
            return None
        if request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user from the request.

        Arguments:
        request -- the Flask request object

        Returns:
        None for now (will be implemented later)
        """
        return None
