import sqlite3
import re

from command.command import Command
from authentication.cancel_booking import CancelBooking


class CancelBookingCommand(Command):

    def __init__(self, cursor, email):
        super().__init__(cursor)
        self.email = email
        self.cb = CancelBooking(cursor)
        
    def main(self):
        bno_cancel = self.display_all_bookings()
        if bno_cancel == -1:
            print()    
        self.cancel_booking(bno_cancel)
    
    def display_all_bookings(self):

        print("Here are all your bookings: ")
        rows = self.cb.get_member_bookings(self.email)
        for i in range(len(rows)):
            print(str(i+1) + ". " + str(rows[i][1:]))
        #bno of booking to cancel
        while(True):
            uinput = input("Which booking would you like to cancel?(n to cancel): ")
            if uinput.lower() == 'n':
                return -1
            try:
                return rows[int(uinput)-1][0]
            except Exception as e:
                print(e)
                print("Invalid Option")
        

    def cancel_booking(self,bno):
        #delete the booking and create a message for the booker
        self.cb.cancel_booking(self.email, bno)
        print('Booking successfully canceled.')
        

    
        

