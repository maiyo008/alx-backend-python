#!/usr/bin/env python3
"""
4-tasks.py
"""
import asyncio
import heapq
from asyncio import Task
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create an asyncio.Task for wait_random and
    execute it n times with the specified max_delay.
    Return the list of delays in ascending order.
    """
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    delays = await asyncio.gather(*tasks)
    sorted_delays = sorted(delays)
    return sorted_delays
