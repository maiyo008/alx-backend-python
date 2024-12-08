import time
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

def retry_on_failure(retries=3, delay=2):
    """
    Decorator that retries a function if it raises an exception,
    with a specified number of retries and a delay between attempts.
    
    Args:
        retries (int): Number of times to retry the function.
        delay (int): Delay in seconds between retry attempts.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    # Try to execute the function
                    return func(*args, **kwargs)
                except sqlite3.Error as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    if attempts < retries:
                        time.sleep(delay)
                    else:
                        print("All retries failed. Operation aborted.")
                        raise
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    """
    Fetches all users from the 'users' table with retry on transient failures.
    
    Args:
        conn (sqlite3.Connection): Active SQLite connection.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# Attempt to fetch users with automatic retry on failure
try:
    users = fetch_users_with_retry()
    print(users)
except sqlite3.Error as e:
    print(f"Final error after retries: {e}")
