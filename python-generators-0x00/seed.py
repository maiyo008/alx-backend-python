#!/usr/bin/python3
"""
Secure MySQL connection using environment variables.
"""
import os
import mysql.connector
import uuid
import csv
from mysql.connector import Error
from dotenv import load_dotenv


load_dotenv()

def connect_db():
    """
    A function to connect to MySQL server
    Returns:
        connection(object): MySQL connection object if successful, else None
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        # if connection.is_connected():
        #     print("MySQL server connected successfully")
        return connection
    except Error as e:
        print(f"Error in connecting to MySQL: {e}")
        return None

def create_database(connection):
    """
    A function to create the ALX_prodev database
    Args:
        connection(object): Connection object to MySQL server
    """
    try:
        mycursor = connection.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        # print("Database ALX_prodev created or already exists")
    except Error as e:
        print(f"Error in creating database: {e}")

def connect_to_prodev():
    """
    A function to connect to the ALX_prodev database
    Returns:
        connection(object): MySQL connection object if successful, else None
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        # if connection.is_connected():
        #     print("Database connected successfully")
        return connection
    except Error as e:
        print(f"Error in connecting to database: {e}")
        return None

def create_table(connection):
    """
    A function to create a table and its required fields
    Args:
        connection(object): Connection object to MySQL server and database
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
        # print("Table 'user_data' created or already exists")
    except Error as e:
        print(f"Error in creating table: {e}")

def insert_data(connection, csv_file):
    """
    Inserts data from a CSV file into the database.
    Args:
        connection(object): Connection object to the database
        csv_file(str): Path to the CSV file
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
        # print("Data inserted successfully")
    except Error as e:
        print(f"Error in inserting data: {e}")

