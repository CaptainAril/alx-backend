#!/usr/bin/env python3
""""""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Returns a turple of integers.

    Args:
        page (int): page index (first page is 1s)
        page_size (int): page content size

    Returns:
        tuple: of size two containing a start index
    and an end index corresponding to the range of indexes to
    return in a list of those particular pagination parameters.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end


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
        """method that returns a paginated page"""
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        start, end = index_range(page, page_size)
        self.dataset()
        try:
            return self.__dataset[start:end]
        except Exception as e:
            return []
