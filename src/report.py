"""Demo fixture: a small, well-specified bug for the issue-to-pull-request demo."""


def page(rows: list, page_number: int, per_page: int = 10) -> list:
    """Return one page of rows. Pages are 1-indexed."""
    start = page_number * per_page
    return rows[start:start + per_page]


def total_pages(rows: list, per_page: int = 10) -> int:
    return len(rows) // per_page
