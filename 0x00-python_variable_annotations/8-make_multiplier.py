#!/usr/bin/env python3
"""Callable"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function"""
    def multiply(n: float):
        """Number"""
        return n * multiplier
    return multiply
