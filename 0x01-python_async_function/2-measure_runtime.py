#!/usr/bin/env python3
"""
2-measure_runtime.py
"""
import time
import asyncio
from typing import Callable
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    and return the average time per execution.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.perf_counter() - start_time

    return elapsed_time / n
