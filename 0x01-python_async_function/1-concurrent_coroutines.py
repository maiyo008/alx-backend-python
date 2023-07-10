#!/usr/bin/env python3
"""
1-concurrent_coroutines.py
"""
import asyncio
import heapq
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute the wait_random coroutine n times with the specified max_delay.
    Return the list of delays in ascending order.
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        heapq.heappush(delays, delay)

    sorted_delays = [heapq.heappop(delays) for _ in range(n)]
    return sorted_delays
