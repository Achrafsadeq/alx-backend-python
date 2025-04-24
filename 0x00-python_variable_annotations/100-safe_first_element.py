#!/usr/bin/env python3
"""
This module provides a function to safely
return the first element of a sequence.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of a sequence, or None if it is empty.

    Args:
        lst (Sequence[Any]): A sequence of any type.

    Returns:
        Union[Any, None]: The first element or None.
    """
    if lst:
        return lst[0]
    else:
        return None
