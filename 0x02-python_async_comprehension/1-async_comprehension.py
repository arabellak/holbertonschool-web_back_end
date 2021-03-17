#!/usr/bin/env python3
"""Async Comprehensions"""
import asyncio
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """Collects 10 randome numbers using an async comprehension"""
    return [i async for i in async_generator()]
