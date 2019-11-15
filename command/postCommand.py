'''
This command module is for posting ride requests
'''
import sqlite3
import re
import sys

from command.command import Command
from post_requests.post_req import PostReq


class PostCommand(Command):

    def __init__(self, cursor, email):
        super().__init__(cursor)
        self.email = email
        self.pr = PostReq(cursor)
        self.values = {'email': email}
        # functions to ask the user for input. Will be asked in this order.
        self.askingFunc = [self.askDate, self.askPickup,
                           self.askDropOff, self.askAmount]

    def menu(self):

        # values of columns
        print('\nRequest Submission: \n')
        print('To go back to main menu at any time, press Ctrl + C\n')

        for func in self.askingFunc:
            if not func():
                return

        self.pr.insert_req(self.values)
        print('Request has been successfully submitted.\n')

    def askDate(self):
        while(True):
            date = input("Please input the date in a YYYY-MM-DD form: ")
            matchObj = re.match("(\d){4}-(0\d|1[0-2])-([0-2]\d|3[0-1])", date)
            if matchObj and matchObj.group() == date:
                self.values['rdate'] = date
                return True
            print('Invalid Date')

    def askPickup(self):
        while(True):
            loc = input("Please input the pick up location code: ")
            if self.pr.validate_location(loc):
                self.values['pickup'] = loc
                return True
            print("Invalid Pickup Location")

    def askDropOff(self):
        while(True):
            loc = input("Please input the drop off location code: ")
            if self.pr.validate_location(loc):
                self.values['dropoff'] = loc
                return True
            print("Invalid Dropoff Location")

    def askAmount(self):
        while(True):
            try:
                inpt = input("Please input your maximum cost per seat: ")
                amnt = int(inpt)
                if amnt < 0:
                    print("Cost cannot be negative.")
                    return False
                self.values['amount'] = amnt
                return True
            except:
                print("Invalid Cost")
