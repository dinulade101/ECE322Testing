from command.command import Command
from command.cancelBookingCommand import CancelBookingCommand
from book_rides.book_rides import BookRides
import sys

class BookingCommand(Command):

    def __init__(self, cursor, email):
        super().__init__(cursor)
        self.email = email

    def menu(self):

        print('\nCreate or Cancel a Booking:\n\nTo go back to main menu at any time, press Ctrl + C\n')

        user_input = input('''Select one of the following: \n
        1) View/Create a booking \n
        2) View/Cancel a booking \n
        quit) Quit\n''')

        while user_input not in ['1', '2']:
            if user_input == 'quit':
                sys.exit(0)
            user_input = input('Invalid input, select from the options mentioned: ')

        if user_input == '1':
            BookRides(self.cursor, self.email).menu()
        if user_input == '2':
            CancelBookingCommand(self.cursor, self.email).menu()
