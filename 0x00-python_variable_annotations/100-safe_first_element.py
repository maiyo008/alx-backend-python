#!/usr/bin/env python3
"""
100-safe_first_element.py
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Duck typing - first element of a sequence
    """
    if lst:
        return lst[0]
    else:
        return None
