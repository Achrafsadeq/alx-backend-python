#!/usr/bin/env python3
"""
This module provides a function that returns a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The number to multiply by.

    Returns:
        Callable[[float], float]: A function
        that multiplies its float argument by the multiplier.
    """
    return lambda x: x * multiplier
