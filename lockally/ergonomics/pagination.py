"""Cursor-pagination helpers."""
from __future__ import annotations

from typing import Callable, Iterator, List, Optional, Tuple, TypeVar

T = TypeVar("T")

# fetch_page(cursor) -> (items, next_cursor). next_cursor is falsy on the last
# page. The Lockally API returns `next_cursor`.
FetchPage = Callable[[str], Tuple[List[T], Optional[str]]]


def paginate(fetch_page: "FetchPage[T]") -> Iterator[T]:
    """Yield every item across all pages.

        for msg in paginate(lambda c: (
            (r := api.list_messages(cursor=c)).data, r.next_cursor
        )):
            print(msg.id)
    """
    cursor = ""
    seen = set()
    while True:
        items, next_cursor = fetch_page(cursor)
        for item in items:
            yield item
        next_cursor = next_cursor or ""
        if not next_cursor or next_cursor == cursor or next_cursor in seen:
            return  # done, or a misbehaving server looping the cursor
        seen.add(cursor)
        cursor = next_cursor


def collect(fetch_page: "FetchPage[T]") -> List[T]:
    """Drain every page into a list. Prefer paginate() for large result sets."""
    return list(paginate(fetch_page))
