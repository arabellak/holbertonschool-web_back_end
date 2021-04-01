#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt


def hash_password(password) -> bytes:
    """Return
        -  A salted, hashed password, which is a byte string.
    """
    password = bytes(password.encode('utf-8'))
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed
