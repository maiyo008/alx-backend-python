#!/usr/bin/python3
"""
"""
import mysql.connector
from mysql.connector import Error


seed = __import__('seed')


def stream_users ():
    """
    """
    seed.load_dotenv()
    connection = seed.connect_to_prodev()
    if connection:
        try:
            mycursor = connection.cursor(dictionary=True)
            mycursor.execute("SELECT * FROM user_data")
            for row in mycursor:
                yield row
        except Error as e:
            print("Error in fetching data: {}".format(e))
        finally:
            mycursor.fetchall()
            mycursor.close()
            connection.close()
    else:
        print('Failed to connect to the database')
