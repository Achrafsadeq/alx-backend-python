#!/usr/bin/env python3
"""
This module measures the runtime of the wait_n coroutine and returns
the average time per task.
"""

import asyncio
import time
from typing import List

# Import the wait_n coroutine from the previous file
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time for wait_n(n, max_delay)
    and return total_time / n.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
