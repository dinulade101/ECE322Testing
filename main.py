import sqlite3
import sys
import os.path
from authentication.member import Member
from search_rides.search_rides import SearchRides
from search_requests.search_requests import SearchRequests
from command.membercommand import MemberCommand

connection = None
cursor = None

cmd = None
user = None

def connect(path):
    global connection, cursor, cmd

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA forteign_keys=ON; ')
    connection.commit()

    cmd = MemberCommand(cursor)
    return

def main():
    global connection, cursor

    db_path = "./prj.db"
    if os.path.isfile(db_path):
        connect(db_path)
    else:
        print('ERROR: database file not found')
        sys.exit(0)

    member = cmd.user()
    member.printUnseenMessages()
    connection.commit()

    connection.commit()
    connection.close()

    return

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nThanks for using rideshare!\n')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
