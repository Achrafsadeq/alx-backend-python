#!/usr/bin/env python3
"""
This module demonstrates running multiple asynchronous tasks concurrently
using task_wait_random and returning their results in sorted order.
"""

import asyncio
from typing import List

# Import task_wait_random from the previous module
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple task_wait_random tasks concurrently
    and return sorted results.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
