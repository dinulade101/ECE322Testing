import sys
from command.command import Command
from command.offerRideCommand import OfferRideCommand
from command.postCommand import PostCommand
from command.searchRequestsCommand import SearchRequestsCommand
from command.bookingCommand import BookingCommand
from search_requests.search_requests import SearchRequests
from search_rides.search_rides import SearchRides
from book_rides.book_rides import BookRides
from command import cancelBookingCommand

class MenuCommand(Command):
    def __init__(self, email, cursor):
        super().__init__(cursor)
        self.user = email
        self.cursor = cursor

    def menu(self):
        opt = input('''Select option!\n
        o/O) Offer ride\n
        s/S) Search rides\n
        b/B) Book or Cancel your bookings\n
        r/R) Make a ride request\n
        v/V) Search or Delete ride requests\n
        l/L) Logout\n
        quit) Quit\n''')

        opt = opt.lower()
        if opt == 'o':
            OfferRideCommand(self.user, self.cursor).menu()
        elif opt == 's':
            search = SearchRides(self.cursor, self.user)
            user_input = input("Please enter 1-3 location key words each seperated by a comma: ").split(',')
            search.find_rides(user_input)
            search.display_rides(0)
        elif opt == 'b':
            BookingCommand( self.cursor, self.user).menu()
        elif opt == 'r':
            PostCommand(self.user,self.cursor).menu()
        elif opt == 'v':
            SearchRequestsCommand(self.cursor, self.user).menu()
        elif opt == 'l':
            return False
        elif opt == 'quit':
            sys.exit(0)
        else:
            print('Invalid option!')
            return self.menu()
        return True
