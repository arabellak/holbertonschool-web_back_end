#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple, List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Contains the star and end index"""
    return (((page - 1) * page_size), (page * page_size))


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Simple pagination"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        ir = index_range(page, page_size)

        return self.dataset()[ir[0]:ir[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns dictionary"""
        dt = len(self.dataset())
        total_pages = math.ceil(dt / page_size)

        dictionary = {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if page + 1 < total_pages else None,
            'prev_page': page - 1 if page - 1 > 0 else None,
            'total_pages': total_pages
        }

        return dictionary
