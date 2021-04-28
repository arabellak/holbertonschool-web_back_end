#!/usr/bin/env python3
"""Strings to Redis
"""
import redis
import uuid
from typing import Any, Callable, Optional, Union
from functool import wraps


def count_calls(method: Callable) -> Callable:
    """
        Decorator count_calls
    """
    k = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        """
        self._redis.incr(k)
        return method(self, *args, **kwds)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
        Store the history of inputs and outputs for a particular function.
    """
    k = method.__qualname__
    inp = k + ":inputs"
    out = k + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
            Wrapper function
        """
        self._redis.rpush(inp, str(args))
        r = method(self, *args, **kwds)
        self._redis.rpush(out, str(r))
        return r
    return wrapper

def replay(method: Callable):
    """
        Display the history of calls of a function
    """
    red = redis.Redis()
    metNam = Cache.store.__qualname__

    inputs = red.lrange("{}:inputs".format(metNam), 0, -1)
    outputs = red.lrange("{}:outputs".format(metNam), 0, -1)

    print("{} was called {} times:".format(metNam,
          red.get(metNam).decode("utf-8")))
    for i, o in tuple(zip(inputs, outputs)):
        print("{}(*('{}',)) -> {}".format(metNam, i.decode("utf-8"),
              o.decode("utf-8")))

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

    @call_history
    @count_calls
    def store(self, data: Any) -> str:
        """
            Generates a random key
        """
        randomKey = str(uuid.uuid4())
        self._redis.set(randomKey, data)
        return randomKey

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[int, bytes, float, str]:
        """
            Get
            Takes a key and callable argument
        """
        if key:
            k = self._redis.get(key)
            return fn(k) if fn else k
