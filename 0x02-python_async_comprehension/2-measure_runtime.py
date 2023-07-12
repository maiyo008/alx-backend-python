#!/usr/bin/env python3
"""
2-measure_runtime.py
Run time for four parallel comprehensions
"""
import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using asyncio.gather.
    Measures the total runtime and returns it.
    """
    s_time = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    e_time = time.perf_counter()
    total_runtime = e_time - s_time

    return total_runtime
