#!/usr/bin/env python3
"""Module for measuring the total runtime of running
   async_comprehension 4 times in parallel."""

import asyncio
import time
from 1_async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """Measure total runtime of executing
     async_comprehension 4 times in parallel."""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start
