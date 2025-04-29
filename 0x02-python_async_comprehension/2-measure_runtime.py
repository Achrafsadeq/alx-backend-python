#!/usr/bin/env python3
"""Module for measuring the total runtime of
   executing async_comprehension in parallel."""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of running
      async_comprehension 4 times in parallel."""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    runtime = time.perf_counter() - start
    return runtime
