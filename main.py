import sqlite3
import sys
import os.path
from authentication.member import Member
from search.search import Search

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
    search = Search(cursor)
    user_input = input().split(',')
    print(user_input)
    search.return_rides(user_input)
    search.display_rides(1)


    connection.commit()
    connection.close()



    return

if __name__ == "__main__":
    main()
