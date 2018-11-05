from command.command import Command
from search_rides.search_rides import SearchRides

class SearchRidesCommand(Command):
    def __init__(self, cursor, email):
        super().__init__(cursor)
        self.user = email

    def menu(self):
        search = SearchRides(self.cursor, self.user)
        print('\nSearch for a Ride:\n\nTo go back to main menu at any time, press Ctrl + C\n')
        user_input = input("Please enter 1-3 location key words each seperated by a comma: ").split(',')
        search.find_rides(user_input)
        search.display_rides(0)
