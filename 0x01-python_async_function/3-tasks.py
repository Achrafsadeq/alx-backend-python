#!/usr/bin/env python3
"""
This module contains a function that creates an asyncio Task from wait_random.
"""

import asyncio

# Import the wait_random coroutine from the previous module
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return an asyncio Task that runs wait_random.

    Args:
        max_delay: Maximum delay for wait_random

    Returns:
        asyncio.Task: Task object for wait_random coroutine
    """
    return asyncio.create_task(wait_random(max_delay))
