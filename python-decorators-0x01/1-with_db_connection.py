import sqlite3
import functools

def with_db_connection(func):
    """
    Decorator that opens a SQLite database connection, 
    passes it to the function, and ensures the connection is closed.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        connection = None
        try:
            # Establish the database connection
            connection = sqlite3.connect("users.db")
            # Pass the connection as the first argument to the wrapped function
            result = func(connection, *args, **kwargs)
            return result
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            if connection:
                # Ensure the connection is closed after the function execution
                connection.close()
    return wrapper

@with_db_connection
def get_user_by_id(conn, user_id):
    """
    Fetch a user by ID from the 'users' table.
    
    Args:
        conn (sqlite3.Connection): Active SQLite connection.
        user_id (int): The ID of the user to fetch.
        
    Returns:
        tuple: The user record as a tuple, or None if not found.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    return cursor.fetchone()

# Fetch user by ID with automatic connection handling
user = get_user_by_id(user_id='97e918d8-14c3-4051-a962-83fbde30203d')
print(user)
