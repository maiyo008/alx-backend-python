lazy_paginator = __import__('2-lazy_paginate')


def stream_user_ages():
    """
    Generator function that fetches user ages one by one.

    Yields:
        int: Age of the user.
    """
    offset = 0
    page_size = 100  # Number of records to fetch per page
    while True:
        page = lazy_paginator.paginate_users(page_size, offset)
        if not page:  # No more data
            break
        for user in page:
            yield user['age']  # Yield user age
        offset += page_size


def calculate_average_age():
    """
    Calculate the average age of users using the stream_user_ages generator.

    Prints:
        str: Average age of users.
    """
    total_age = 0
    count = 0

    for age in stream_user_ages():
        total_age += age
        count += 1

    if count > 0:
        average_age = total_age / count
        print(f"Average age of users: {average_age:.2f}")
    else:
        print("No users found.")
