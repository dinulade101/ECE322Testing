import sqlite3
import re

from command.command import Command
from authentication.cancel_booking import CancelBooking


class CancelBookingCommand(Command):

    def __init__(self, cursor, email):
        super().__init__(cursor)
        self.email = email
        self.cb = CancelBooking(cursor)
        
    def display_all_bookings(self):
        print("Here are all your bookings: ")
        rows = self.cb.get_member_bookings(self.email)
        for i in range(len(rows)):
            print(str(i+1) + ". " + str(rows[i][1:]))

    def cancel_booking(self,bno):
        #delete the booking and create a message for the booker
        pass

    
        

