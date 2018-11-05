'''
This file deals with all the commands to allow the user to cancel bookings.
It will initially display all the user's bookings. Then the user will select 
the number of the booking displayed to cancel. The row of the booking in the db
will be removed. The member who's booking was canceled will get an automated message
as well.
'''
import sqlite3
import re
import sys

from command.command import Command
from book_rides.cancel_booking import CancelBooking

class CancelBookingCommand(Command):

    def __init__(self, cursor, email):
        super().__init__(cursor)
        self.email = email
        self.cb = CancelBooking(cursor)
        

    def menu(self):
        
        print('Welcome to the bookings page.')
        print('Type "quit" to exit program')
        print('Press Ctrl-c to return to menu')

        rows = self.cb.get_member_bookings(self.email)

        if len(rows) == 0:
            print("You do not have any bookings.")
            return
        valid_bno = set()
        for row in rows:
            valid_bno.add(row[0])
        
        self.display_page(0, rows, valid_bno)


    def cancel_booking(self,bno):
        #delete the booking and create a message for the booker
        self.cb.cancel_booking(self.email, bno)
        print('Booking successfully canceled.')
    
    def display_page(self, page_num, rows, valid_bno):
        page = rows[page_num*5: min(page_num*5+5, len(rows))]
        for row in page:
            print(str(row[0]) + '.', end='')
            print(row[1:])
        if (page_num*5+5 < len(rows)):
            user_input = input("To delete a booking, please enter the booking number. To see more bookings enter (y/n)?")
            if user_input == 'quit':
                sys.exit()
            if (user_input == 'y'):
                self.display_page(page_num+1, rows, valid_bno)
                return
        else:
            user_input = input("To cancel a booking, please enter the booking number: ")
            if user_input == 'quit':
                sys.exit()
        if user_input.isdigit() and int(user_input) in valid_bno:
            print("Canceled the following booking with bno: " + user_input)
            self.cancel_booking(user_input)
        else:
            print("Invalid number entered")