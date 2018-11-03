import sqlite3
import sys
import os.path
from authentication.member import Member
from search_rides.search_rides import SearchRides
from search_requests.search_requests import SearchRequests

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
    '''search = SearchRides(cursor)
    user_input = input().split(',')
    search.find_rides(user_input)
    search.display_rides(0)'''

    search_requests = SearchRequests(cursor, "darryl@oil.com")
    user_input = input("To search by pickup location, please enter a pickup location code. Otherwise, to view all requests, press Enter to continue.")
    if user_input:
        search_requests.find_requests(user_input)
    else:
        search_requests.find_requests()
        
    search_requests.display_results(0)
    

    connection.commit()
    connection.close()

    return

if __name__ == "__main__":
    main()
