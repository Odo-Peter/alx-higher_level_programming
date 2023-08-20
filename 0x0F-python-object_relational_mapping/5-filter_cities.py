#!/usr/bin/python3
'''
script that takes in the name of a state as an argument,
queries and lists all cities in state
'''

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306,
                         host='localhost')

    cursor = db.cursor()
    cursor.execute(
        'SELECT cities.name FROM cities\
        INNER JOIN states ON cities.state_id = states.id\
        WHERE states.name = %s \
        ORDER BY cities.id ASC', (sys.argv[4], ))

    cities = cursor.fetchall()

    indx = 0
    for city in cities:
        if indx != 0:
            print(", ", end="")
        print("%s" % city, end="")
        indx += 1
    print("")

    cursor.close()
    db.close()
