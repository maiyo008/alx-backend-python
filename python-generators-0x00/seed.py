#!/usr/bin/python3
"""
"""
import mysql.connector
import uuid
from mysql.connector import Error
import csv


def connect_db():
    """
    A function to connect to mysql database
    Returns:
        connection object if connection is successful else None
    """
    try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@tengecha4N"
    )
        if connection.is_connected():
            print("mysql server connected successfuly")
        return connection
    except Error as e:
        print('Error in connecting to mysql: {}'.format(e))
        return None

def create_database(connection):
    """
    A function that creates the function ALX_prodev
    Args:
        connection(object) - connection object used to connect to mysql server
    Returns:
        None
    """
    try:
        mycursor = connection.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodec created or already exists")
    except Error as e:
        print('Error in creating database: '.format(e))

def connect_to_prodev():
    """
    A function that connects to ALX_prodev database
    Returns:
        connection(obj) - Connection object if connection is a success else None
    """
    try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@tengecha4N",
        database="ALX_prodev"
    )
        if connection.is_connected():
            print("Database connected successfuly")
        return connection
    except Error as e:
        print('Error in connecting to database: {}'.format(e))
        return None

def create_table(connection):
    """
    A function that creates a table and its required fields
    Args:
        connection(obj): connection object to mysql server and db
    """
    try:
        mycursor = connection.cursor()
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY NOT NULL,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL(3, 0) NOT NULL,
                INDEX (user_id)
            )
        """)
        print('user_table created or exists')
    except Error as e:
        print('Error in creating table: {}'.format(e))

def insert_data(connection, csv_file):
    """
    """
    try:
        mycursor = connection.cursor()
        insert_query = """
           INSERT INTO user_data (user_id, name, email, age)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE name=name 
        """
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                user_id = str(uuid.uuid4())
                mycursor.execute(insert_query, (user_id, row['name'], row['email'], row['age']))
        connection.commit()
        print('Data inserted successfully')
    except Error as e:
        print('Error in inserting data: {}'.format(e))

