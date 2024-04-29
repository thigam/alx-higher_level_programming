#!/usr/bin/python3
"""
Contains a script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

def main():
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON states.id=cities.state_id ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)

if __name__=="__main__":
    main()
