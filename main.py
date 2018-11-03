import sqlite3
import sys
import os.path
from authentication.member import Member
from command.memberCommand import MemberCommand

import post_ride
connection = None
cursor = None

mCmd = None

user = None

def connect(path):
    global connection, cursor, mCmd

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA forteign_keys=ON; ')
    connection.create_function('HASH', 1, Member.hash)
    connection.commit()

    mCmd = MemberCommand(cursor)

    return

def main():
    global connection, cursor

    db_path = "./prj.db"
    if os.path.isfile(db_path):
        connect(db_path)
    else:
        print('ERROR: database file not found')
        sys.exit(0)

    member = mCmd.user()

    connection.commit()
    connection.close()
    return

def test():
    pr = post_ride.PostRide(cursor)
    print(pr.validate_location("YEG"))
if __name__ == "__main__":
    main()
