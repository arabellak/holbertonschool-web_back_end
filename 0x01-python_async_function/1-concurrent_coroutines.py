#!/usr/bin/env python3
"""Multiple coroutines at the same time with async"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with max_delay"""
    delay = []
    for i in range(n):
        delay.append(asyncio.create_task(wait_random(max_delay)))
    return [await j for j in asyncio.as_completed(delay)]
