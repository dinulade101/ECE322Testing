from command.command import Command
from search_rides.search_rides import SearchRides

class SearchRidesCommand(Command):
    def __init__(self, cursor, user):
        super().__init__(cursor)
        self.user = user

    def menu(self):
        search = SearchRides(self.cursor, self.user)
        print('\nSearch for a Ride:\n\nTo go back to main menu at any time, press Ctrl + C\n')
        user_input = input("Please enter 1-3 location key words each seperated by a comma: ").split(',')
        if (len(user_input) > 3 or len(user_input) == 0 or user_input[0] == ''):
            print("Please enter a valid set of key words. Otherwise, to return to main menu press Ctrl + C")
            self.menu()
            return
        for index in range(len(user_input)):
            user_input[index] = user_input[index].strip()

        search.find_rides(user_input)
