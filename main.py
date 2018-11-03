import sqlite3
import sys
import os.path
from authentication.member import Member
from command.memberCommand import MemberCommand
from command.postCommand import PostCommand
from command.cancelBookingCommand import CancelBookingCommand 




connection = None
cursor = None

mCmd = None
pCmd = None
cbCmd = None

user = None

def connect(path):
    global connection, cursor, mCmd, pCmd, cbCmd

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA forteign_keys=ON; ')
    connection.create_function('HASH', 1, Member.hash)
    connection.commit()

    mCmd = MemberCommand(cursor)
    pCmd = PostCommand(cursor, "kenboo1998@gmail.com")
    cbCmd = CancelBookingCommand(cursor, "bob@123.ca")

    return

def main():
    global connection, cursor

    db_path = "./prj.db"
    if os.path.isfile(db_path):
        connect(db_path)
    else:
        print('ERROR: database file not found')
        sys.exit(0)

    cbCmd.displayAllBookings()

    connection.commit()
    connection.close()
    return

if __name__ == "__main__":
    main()
