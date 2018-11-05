import sys
from command.command import Command
from command.offerRideCommand import OfferRideCommand
from search_requests.search_requests import SearchRequests
from search_rides.search_rides import SearchRides

class MenuCommand(Command):
    def __init__(self, email, cursor):
        super().__init__(cursor)
        self.user = email
        self.cursor = cursor

    def menu(self):
        opt = input('''Select option!\n
        o/O) Offer ride\n
        s/S) Search rides\n
        b/B) Book or cancel your bookings\n
        r/R) Make a ride request\n
        v/V) Search or delete ride requests\n
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
            pass
        elif opt == 'r':
            pass
        elif opt == 'v':
            search = SearchRequests(self.cursor, self.user)
            user_input = input('''Select one of the following: \n 1) View and modify your ride requests \n 2) View ride requests by location \n''')
            if user_input == '1':
                search.find_requests()
                search.display_results(0)
            elif user_input == '2':
                location = input("Please enter a lcode or city name: ")
                search.find_requests_by_location(location)
                search.display_results_location(0)
        elif opt == 'l':
            return False
        elif opt == 'quit':
            sys.exit(0)
        else:
            print('Invalid option!')
            return self.menu()
        return True
