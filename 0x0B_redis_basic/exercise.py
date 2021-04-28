#!/usr/bin/env python3
"""Strings to Redis
"""
import redis
import uuid
from typing import Any


class Cache():
    """
        Cache class
    """
    def __init__(self):
        """
            Init method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """
            Generates a random key
        """
        randomKey = str(uuid.uuid4())
        self._redis.set(randomKey, data)
        return randomKey
