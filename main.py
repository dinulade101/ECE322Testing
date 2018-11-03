import sqlite3
import sys
import os.path
from authentication.member import Member
<<<<<<< HEAD
from command.membercommand import MemberCommand
import post_ride
from search_rides.search_rides import SearchRides
from search_requests.search_requests import SearchRequests
=======
from command.memberCommand import MemberCommand
from command.postCommand import PostCommand
from command.cancelBookingCommand import CancelBookingCommand



>>>>>>> ea9651d9dc9b96bfce735a29b78ba7387436c600

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

    member = mCmd.user()
    member.printUnseenMessages()
    connection.commit()

    # '''search = SearchRides(cursor)
    # user_input = input().split(',')
    # search.find_rides(user_input)
    # search.display_rides(0)'''
    #
    # search_requests = SearchRequests(cursor, "darryl@oil.com")
    # user_input = input("To search by pickup location, please enter a pickup location code. Otherwise, to view all requests, press Enter to continue.")
    # if user_input:
    #     search_requests.find_requests(user_input)
    # else:
    #     search_requests.find_requests()
    #
    # search_requests.display_results(0)

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
