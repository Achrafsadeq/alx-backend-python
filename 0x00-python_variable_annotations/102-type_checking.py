#!/usr/bin/env python3
"""
This module provides a function to zoom a sequence by repeating elements.
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Return a zoomed list with each element repeated `factor` times.

    Args:
        lst: The original sequence of integers.
        factor: Repetition factor. Defaults to 2.

    Returns:
        A list with repeated elements.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
