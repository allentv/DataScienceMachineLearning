# -*- coding: utf-8 -*-
"""
This is a tutorial for interacting with a database in python.
Before you execute this script, make sure you have MySQL database and its drivers installed.
Create a test database with a test table having some records.

Created on Wed Jul 15 13:22:10 2015
@author: Allen Thomas Varghese
"""

import MySQLdb  # On error, try pip install mysql-python


def test_mysql():
    # Connect to the MySQL database with the specified parameters
    db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='tutorial')

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


    # Using a dictionary cursor
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    print "Executing the query to get the record count in 'test_table'"
    cursor.execute('SELECT COUNT(*) AS rec_count FROM test_table')
    print "Number of records is %s" % cursor.fetchone()['rec_count']

    cursor.execute("SELECT * FROM test_table")
    for rec in cursor.fetchall():
        print rec
        # print rec['PK'], rec['random_number'], rec['comment']

    # Close the database connection
    db.close()


if __name__ == '__main__':
    test_mysql()
