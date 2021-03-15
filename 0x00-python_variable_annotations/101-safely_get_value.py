#!/usr/bin/env python3
"""Type annotations"""


from typing import TypeVar, Mapping, Any, Union


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[TypeVar('T'), None]
                     ) -> Union[Any, TypeVar('T')]:
    """Given code"""
    if key in dct:
        return dct[key]
    else:
        return default
