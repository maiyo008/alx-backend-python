#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error


seed = __import__('seed')


def stream_users_in_batches(batch_size):
    """
    A generator function to fetch rows in batches from the user_data table.
    
    Args:
        batch_size (int): Number of rows to fetch per batch.
    
    Returns:
        List[dict]: A list of user records fetched in the batch.
    """
    seed.load_dotenv()
    connection = seed.connect_to_prodev()
    print('Database connected')
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)

            offset = 0
            while True:
                cursor.execute(
                    f"SELECT * FROM user_data LIMIT {batch_size} OFFSET {offset}"
                )
                batch = cursor.fetchall()
                if not batch:
                    break
                yield batch
                offset += batch_size

        except Error as e:
            print(f"Error in fetching data: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    else:
        print('Failed to connect to the database')

def batch_processing(batch_size):
    """
    Processes each batch to filter users over the age of 25.
    
    Args:
        batch_size (int): Number of rows to process per batch.
    
    Yields:
        dict: A user record with age > 25.
    """
    print(batch_size)
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
