#!/usr/bin/env python3
"""Multiple coroutines at the same time with async"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with max_delay"""
    delay = []
    for i in range(n):
        delay.append(task_wait_random(max_delay))
    return [await j for j in asyncio.as_completed(delay)]
