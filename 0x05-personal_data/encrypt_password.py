#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt


def hash_password(password):
    """Return
        -  A salted, hashed password, which is a byte string.
    """
    password = b'secret psswd'
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
