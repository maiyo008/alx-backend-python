#!/usr/bin/python3
seed = __import__('seed')


def paginate_users(page_size, offset):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_paginate(page_size):
    """
    Generator function to lazily fetch paginated data from the database.

    Args:
        page_size (int): Number of rows to fetch per page.

    Yields:
        list[dict]: A list of user records for the current page.
    """
    offset = 0  # Initialize the offset to 0

    while True:
        page = paginate_users(page_size, offset)  # Fetch the current page
        if not page:  # If no rows are returned, exit the loop
            break
        yield page  # Yield the current page
        offset += page_size  # Increment the offset by page_size
