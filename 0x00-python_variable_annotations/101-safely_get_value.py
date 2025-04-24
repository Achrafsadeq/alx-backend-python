#!/usr/bin/env python3
"""
This module provides a function to safely retrieve a value from a dictionary.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely get a value from a dictionary with a fallback default.

    Args:
        dct (Mapping): The dictionary.
        key (Any): The key to look for.
        default (Union[T, None], optional): The fallback value.
                                            Defaults to None.

    Returns:
        Union[Any, T]: The value if found, otherwise the default.
    """
    if key in dct:
        return dct[key]
    return default
