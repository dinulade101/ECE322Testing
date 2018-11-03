import sqlite3
import sys
import os.path
from authentication.member import Member
from command.memberCommand import MemberCommand

connection = None
cursor = None

mCmd = None

user = None

def connect(path):
    global connection, cursor, mCmd

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA forteign_keys=ON; ')
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
