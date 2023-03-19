#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306, host="localhost")

    # Create a cursor object
    cursor = db.cursor()

    # Execute a SQL query to select all rows from the states table and order them 
    # by id in ascending order
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows from the cursor
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and database connections
    cursor.close()
    db.close()
