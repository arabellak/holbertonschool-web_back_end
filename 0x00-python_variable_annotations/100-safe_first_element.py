# The types of the elements of the input are not know
"""Corrects duck-type annotations"""


from typing import List, Any, Union


def safe_first_element(lst: List[Any]) ->  Union[Any, None]:
    """Duck-type"""
    if lst:
        return lst[0]
    else:
        return None
