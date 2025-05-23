#!/usr/bin/env python3
"""
Module to hash passwords securely using bcrypt with salt.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password with a generated salt using bcrypt
    and returns the hashed password as bytes.

    Args:
        password (str): The plain text password to hash.

    Returns:
        bytes: The salted, hashed password.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates a password against a hashed password.

    Args:
        hashed_password (bytes): The hashed password to validate against.
        password (str): The plain text password to validate.

    Returns:
        bool: True if the password matches the hash, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
