#!/usr/bin/env python3
"""Module for collecting 10 values from async_generator
   using async comprehension."""

from typing import List
from 0_async_generator import async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers
       asynchronously from async_generator."""
    return [i async for i in async_generator()]
