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
    sql = "SELECT cities.name \
            FROM cities INNER JOIN states \
            ON cities.state_id = states.id \
            WHERE states.name LIKE BINARY %s \
            ORDER BY cities.id ASC"
    cur.execute(sql, (state_name,))
    rows = cur.fetchall()
    print_it = [row[0] for row in rows]
    print(*print_it, sep=", ")
