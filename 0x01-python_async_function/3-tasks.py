#!/usr/bin/env python3
"""
3-tasks.py
"""
from asyncio import Task
from typing import Callable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Create an asyncio.Task that runs the wait_random coroutine
    with the specified max_delay.Return the asyncio.Task object.
    """
    return Task(wait_random(max_delay))
