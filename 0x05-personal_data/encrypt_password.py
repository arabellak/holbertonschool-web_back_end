#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Return
        -  A salted, hashed password, which is a byte string.
    """
    password = bytes(password.encode('utf-8'))
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Provided password matches the hashed password
    """
    password = bytes(password.encode('utf-8'))
    return bcrypt.checkpw(password, hashed_password)
