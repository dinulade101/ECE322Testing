from command.command import Command
from search_requests.search_requests import SearchRequests
import sys

class SearchRequestsCommand(Command):
    def __init__(self, cursor, email):
        super().__init__(cursor)
        self.user = email

    def menu(self):
        search = SearchRequests(self.cursor, self.user)
        print('\nSearch/Delete ride requests:\n\nTo go back to main menu at any time, press Ctrl + C\n')

        user_input = input('''Select an option:\n
        1) View and modify your ride requests\n
        2) View ride requests by location\n
        quit) Quit\n''')

        if user_input == '1':
            search.find_requests()
            search.display_results(0)
        elif user_input == '2':
            location = input("Please enter a lcode or city name: ")
            search.find_requests_by_location(location)
        elif user_input == 'quit':
            sys.exit(0)
