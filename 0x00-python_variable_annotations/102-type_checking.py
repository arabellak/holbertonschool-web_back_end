#!/usr/bin/env python3
"""Type Checking"""


from typing import Tuple, List
import math


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Given code"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, math.floor(3.0))