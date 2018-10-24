import sqlite3
import os.path
import sys

connection = None
cursor = None

def connect(path):
    global connection, cursor

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA forteign_keys=ON; ')
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

    connection.commit()
    connection.close()
    return

if __name__ == "__main__":
    main()
