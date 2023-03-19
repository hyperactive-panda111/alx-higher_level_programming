#!/usr/bin/env python3
import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Connect to the database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    # Create a cursor object
    cur = conn.cursor()

    # Execute the query to get all states sorted by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows and print them out
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    conn.close()
