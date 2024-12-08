import sqlite3
import functools

# Global dictionary to store cached query results
query_cache = {}

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
            return func(connection, *args, **kwargs)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            if connection:
                # Ensure the connection is closed after the function execution
                connection.close()
    return wrapper

def cache_query(func):
    """
    Decorator to cache query results based on the SQL query string.
    If the query has been executed before, return the cached result.
    """
    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        # Check if the query is already cached
        if query in query_cache:
            print(f"Using cached result for query: {query}")
            return query_cache[query]

        # Execute the query and cache the result
        print(f"Executing query and caching result: {query}")
        result = func(conn, query, *args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    """
    Fetches data from the database based on the provided SQL query.
    Results are cached to avoid redundant queries.
    """
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call will execute the query and cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")
print(users)

# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print(users_again)
