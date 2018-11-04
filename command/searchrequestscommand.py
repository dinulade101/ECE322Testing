from command.command import Command 
from search_requests.search_requests import SearchRequests

class SearchRequestsCommand(Command)
    def __init__(self, cursor):
        super().__init__(cursor)
    
    def menu(self):
        search_requests = SearchRequests(cursor, "darryl@oil.com")
        user_input = input("To search by pickup location, please enter a pickup location code. Otherwise, to view all requests, press Enter to continue.")
        if user_input:
            search_requests.find_requests(user_input)
        else:
            search_requests.find_requests()
        
        search_requests.display_results(0)