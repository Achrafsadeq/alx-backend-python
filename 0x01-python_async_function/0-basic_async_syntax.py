#!/usr/bin/env python3
"""
This is a Python script that demonstrates asynchronous programming
using asyncio.
It defines a coroutine that waits for a random amount of time.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay seconds.

    Args:
        max_delay: Maximum delay in seconds (default: 10)

    Returns:
        float: The actual delay time (in seconds) that was waited
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
