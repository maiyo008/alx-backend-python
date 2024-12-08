#!/usr/bin/python3
"""
Load data into a SQLite database from a CSV file.
"""
import sqlite3
import uuid
import csv
import os


def connect_to_database(db_name="users.db"):
    """
    Connects to the SQLite database (or creates it if it doesn't exist).
    
    Args:
        db_name (str): The name of the SQLite database file.
        
    Returns:
        connection (object): SQLite connection object.
    """
    try:
        connection = sqlite3.connect(db_name)
        print(f"Connected to SQLite database: {db_name}")
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to SQLite database: {e}")
        return None


def create_users_table(connection):
    """
    Creates the 'users' table if it doesn't already exist.
    
    Args:
        connection (object): SQLite connection object.
    """
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        """)
        print("Table 'users' created or already exists.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")


def insert_data_from_csv(connection, csv_file):
    """
    Inserts data into the 'users' table from a CSV file.
    
    Args:
        connection (object): SQLite connection object.
        csv_file (str): Path to the CSV file.
    """
    try:
        cursor = connection.cursor()
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                user_id = str(uuid.uuid4())  # Generate a unique user ID
                cursor.execute("""
                    INSERT INTO users (user_id, name, email, age)
                    VALUES (?, ?, ?, ?)
                """, (user_id, row['name'], row['email'], int(row['age'])))
        connection.commit()
        print("Data inserted successfully from CSV.")
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")
    except Exception as e:
        print(f"General error: {e}")


if __name__ == "__main__":
    # Database file
    db_file = "users.db"

    # Path to your CSV file
    csv_file = "../python-generators-0x00/user_data.csv"

    # Connect to SQLite database
    connection = connect_to_database(db_file)

    if connection:
        # Create 'users' table
        create_users_table(connection)

        # Insert data from CSV
        if os.path.exists(csv_file):
            insert_data_from_csv(connection, csv_file)
        else:
            print(f"CSV file '{csv_file}' not found.")

        # Close the database connection
        connection.close()
