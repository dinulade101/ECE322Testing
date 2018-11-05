from command.command import Command
from search_rides.search_rides import SearchRides

class SearchRidesCommand(Command):
    def __init__(self, cursor):
        super().__init__(cursor)

    def menu(self):
        search = SearchRides(cursor)
        user_input = input().split(',')
        search.find_rides(user_input)
        search.display_rides(0)
