#!/usr/bin/env python3
"""
This module demonstrates running multiple asynchronous tasks concurrently
and returning their results in sorted order.
"""

import asyncio
from typing import List

# Import the wait_random coroutine from another module
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple wait_random coroutines concurrently
    and return sorted results.
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
