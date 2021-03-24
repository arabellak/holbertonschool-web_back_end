#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Contains the star and end index"""
    return ((page - 1), (page_size - 1))
