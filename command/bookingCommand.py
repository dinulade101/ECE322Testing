from command.command import Command
from command.cancelBookingCommand import CancelBookingCommand
from book_rides.book_rides import BookRides

class BookingCommand(Command):

    def __init__(self, cursor, email):
        super().__init__(cursor)
        self.email = email

    def menu(self):


        while(True):
            print('\nCreate or Cancel a Booking:\n\nTo go back to main menu at any time, press Ctrl + C\n')
            user_input = input('''Select one of the following: \n
            1) Create a booking \n
            2) Cancel a booking \n''')
            if user_input == 'quit':
                return
            if user_input.isdigit():
                if user_input == '1':
                    BookRides(self.cursor, self.email).menu()
                if user_input == '2':
                    CancelBookingCommand(self.cursor, self.email).menu()
                else:
                    print('Not a valid option')
            else:
                print('Not a valid input')
