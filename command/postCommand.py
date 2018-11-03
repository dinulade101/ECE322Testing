import sqlite3
import re

from command.command import Command
from authentication.post_req import PostReq


class PostCommand(Command):

    def __init__(self, cursor, email):
        super().__init__(cursor)
        self.email = email
        self.pr = PostReq(cursor)
        self.values = {'email':email}
        # functions to ask the user for input. Will be asked in thisd order.
        self.askingFunc = [self.askDate, self.askPickup, self.askDropOff, self.askAmount]
    
    def askDate(self):
        date = input("Please input the date in a YYYY-MM-DD form: ")
        matchObj = re.match("(\d){4}-[0-1]\d-[0-3]\d", date)
        if matchObj and matchObj.group() == date:
            self.values['rdate'] = date
            return True
        else:
            print('Not a valid date')
            return False

    def askPickup(self):
        loc = input("Please input the 5 pick up location code: ")
        if self.pr.validate_location(loc):
            self.values['pickup'] = loc
            return True
        else:
            print("Not a Valid Location")
            return False

    def askDropOff(self):
        loc = input("Please input the 5 destination location code: ")
        if self.pr.validate_location(loc):
            self.values['dropoff'] = loc
            return True
        else:
            print("Not a Valid Location")
            return False
    
    def askAmount(self):
        try:
            amnt = int(input("Please input your maximum cost per seat: "))
            if amnt < 0:
                print("Cost cannot be negative.")
                return False
            self.values['amount'] = amnt
            return True
        except:
            print("Not a valid cost.")
            return False
        


    def ask(self):
        print("-----------Make a Request-------------")
        # values of columns
        for func in self.askingFunc:
            if not func():
                return
        
        self.pr.insert_req(self.values)
