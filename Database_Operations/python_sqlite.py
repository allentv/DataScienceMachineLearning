# -*- coding: utf-8 -*-
"""
This is a tutorial for interacting with a database in python.
Before you execute this script, make sure you have a sqlite database.
Create a test database with a test table having some records.

Created on Wed Jul 15 13:22:10 2015
@author: Allen Thomas Varghese
"""

import sqlite3  # Bundled with Python


def create_sqlite_db():
    # Connect to the sqlite database with the specified parameters
    db = sqlite3.connect('test_sqlite.db')
    cursor = db.cursor()
    try:
        # If table exists, drop it
        cursor.execute("DROP TABLE `test_table`")
    except sqlite3.OperationalError:
        pass

    # Create the table
    cursor.execute("""
        CREATE TABLE `test_table` (
          PK int(11) NOT NULL PRIMARY KEY,
          random_number int(11) DEFAULT NULL,
          comment varchar(45) DEFAULT NULL
        )
    """)

    # Insert 10 records in the table
    for number in range(1, 11):
        cursor.execute(
            "INSERT INTO test_table VALUES (?, ?, ?)",
            (number, number * 10, 'c%s' % number)
        )

    # Save all the changes
    db.commit()
    db.close()


def test_sqlite():
    # Connect to the sqlite database with the specified parameters
    db = sqlite3.connect('test_sqlite.db')

    # Get access to a cursor object for interacting with the database
    cursor = db.cursor()

    # Execute a query to get the number of records from a table
    print "Executing the query to get the record count in 'test_table'"
    cursor.execute('SELECT COUNT(*) AS rec_count FROM test_table')
    # The result is a tuple with only one value. So get the value at index 0
    print "Number of records is %s" % cursor.fetchone()[0]


    # Execute a query to print out all the records from the table
    cursor.execute("SELECT * FROM test_table")
    for rec in cursor.fetchall():
        print rec
        # print rec[0], rec[1], rec[2]

    # Close the database connection
    db.close()


if __name__ == '__main__':
    create_sqlite_db()
    test_sqlite()
