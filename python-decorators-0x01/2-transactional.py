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

def transactional(func):
    """
    Decorator that wraps a function inside a database transaction.
    Automatically commits the transaction if the function succeeds,
    or rolls back the transaction if an error occurs.
    """
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            # Execute the wrapped function
            result = func(conn, *args, **kwargs)
            # Commit the transaction on success
            conn.commit()
            return result
        except sqlite3.Error as e:
            # Roll back the transaction on error
            conn.rollback()
            print(f"Transaction failed: {e}")
            return None
    return wrapper

@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    """
    Updates a user's email address in the 'users' table.
    
    Args:
        conn (sqlite3.Connection): Active SQLite connection.
        user_id (int): The ID of the user to update.
        new_email (str): The new email address.
    """
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE user_id = ?", (new_email, user_id))

# Update user's email with automatic transaction handling
update_user_email(user_id='97e918d8-14c3-4051-a962-83fbde30203d', new_email='Crawford_Cartwright@hotmail.com')
