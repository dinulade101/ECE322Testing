import sqlite3
import sys
import os.path
from authentication.member import Member

import post_ride
connection = None
cursor = None

user = None

def connect(path):
    global connection, cursor

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA forteign_keys=ON; ')
    connection.create_function('HASH', 1, Member.hash)
    connection.commit()
    return

def main():
    global connection, cursor

    db_path = "./prj.db"
    if os.path.isfile(db_path):
        connect(db_path)
    else:
        print('ERROR: database file not found')
        sys.exit(0)

    # member = command.user()
    test()
    connection.commit()
    connection.close()
    return

def test():
    pr = post_ride.PostRide(cursor)
    print(pr.validate_location("YEG"))
if __name__ == "__main__":
    main()
