#!/usr/bin/env python3
"""Simple helper function."""


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
