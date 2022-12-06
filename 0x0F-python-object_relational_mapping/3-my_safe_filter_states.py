#!/usr/bin/python3
''' a script that lists all states from the database hbtn_0e_0_usa'''
import MySQLdb
from sys import argv


if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(
            'localhost',
            mysql_username,
            mysql_password,
            database_name
            )
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name LIKE BINARY '{}'"
    cur.execute(sql.format(state_name))
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
