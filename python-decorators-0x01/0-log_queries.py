import sqlite3
import functools

def log_queries():
    """
    Decorator to log SQL queries before executing them.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if 'query' in kwargs:
                print(f"Executing SQL query: {kwargs['query']}")
            elif len(args) > 0 and isinstance(args[0], str):
                print(f"Executing SQL query: {args[0]}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_queries()
def fetch_all_users(query):
    """
    Fetches all users from the database.
    Logs the query before execution using the log_queries decorator.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
for user in users:
    print(user)
