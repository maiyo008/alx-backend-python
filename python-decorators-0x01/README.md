# **Python Decorators Project**

---

## **Overview**

This project demonstrates the use of Python decorators for managing database operations. By leveraging decorators, we ensure cleaner, reusable, and more efficient code for handling common database-related tasks.

---

## **Objectives**

1. **Database Connection Management**  
   Automatically open and close database connections for any function.

2. **Transaction Handling**  
   Commit or rollback database changes automatically based on function execution success or failure.

3. **Retry Mechanism**  
   Retry database queries in case of transient errors.

4. **Query Caching**  
   Cache query results to optimize performance and reduce redundant database calls.

---

## **Implemented Decorators**

### **1. Managing Database Connections**

**Decorator**: `with_db_connection`  
**Functionality**: Opens a database connection before the function call and closes it after the function completes.

```python
@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

# Usage
user = get_user_by_id(user_id=1)
print(user)
