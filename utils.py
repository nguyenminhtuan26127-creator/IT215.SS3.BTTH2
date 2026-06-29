def get_return_book(books: list, is_available: bool) -> list:
    """
    Filter books by availability status.

    Args:
        books (list): List of book dictionaries.
        is_available (bool): True to get available books, False to get borrowed books.

    Returns:
        list: Filtered list of books.
    """
    return [book for book in books if book.get("is_available") == is_available]