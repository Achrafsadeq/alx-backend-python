#!/usr/bin/env python3
"""
This module provides a function that returns
a tuple with a string and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple where the first element is a string and 
    the second is the square of a number.

    Args:
        k (str): A string key.
        v (Union[int, float]): A value to be squared.

    Returns:
        Tuple[str, float]: A tuple of the string 
        and squared value as float.
    """
    return (k, float(v * v))
