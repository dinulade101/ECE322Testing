import sqlite3
import sys
import os.path
from authentication.member import Member
from command.membercommand import MemberCommand
from command.menucommand import MenuCommand

connection = None
cursor = None

cmd = None
user = None

def connect(path):
    global connection, cursor, user

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA forteign_keys=ON; ')
    user = Member(None, None, cursor)
    connection.commit()
    return

def main():
    global connection, cursor, cmd, user

    db_path = "./prj.db"
    if os.path.isfile(db_path):
        connect(db_path)
    else:
        print('ERROR: database file not found')
        sys.exit(0)

    while True:
        if not user.isLoggedIn():
            cmd = MemberCommand(cursor)
            user = cmd.user()
            user.printUnseenMessages()
            connection.commit()
        else:
            cmd = MenuCommand(cursor)
            if not cmd.menu():
                user.logout()
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
