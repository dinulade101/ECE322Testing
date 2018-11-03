class SearchRequests:
    def __init__(self, cursor, email):
        self.requests = []
        self.email = email
        self.cursor = cursor
    def find_requests(self, location):
        search_query = '''SELECT r.*
        FROM requests r, locations l
        WHERE l.lcode = r.pickup
        AND r.email = '{email}'
        AND (l.lcode = '{location}'
        OR l.city = '{location}'
        ) COLLATE NOCASE
        '''.format(email = self.email, location = location)

        self.cursor.execute(search_query)
        self.requests = self.cursor.fetchall()

    def find_requests(self):
        search_query = '''SELECT r.*
        FROM requests r, locations l
        WHERE l.lcode = r.pickup
        AND r.email = '{email}'
        '''.format(email = self.email)

        self.cursor.execute(search_query)
        self.requests = self.cursor.fetchall()

    def display_results(self, page_num):
        page = self.requests[page_num*5: min(page_num*5+5, len(self.requests))]
        for ride in page:
            print(str(ride[0]) + '.', end='')
            print(ride[1:])
        if (page_num*5+5 < len(self.requests)):
            user_input = input("To delete a request, please enter the reqest number. To see more requests more requests enter (y/n)?")
            if (user_input == 'y'):
                self.display_results(page_num+1)
        else:
            user_input = input("To delete a request, please enter the reqest number: ")
        if user_input.isdigit():
            print("Deleted the following request with rid: " + user_input)
            delete_query = "DELETE FROM requests WHERE rid = {rid}".format(rid = user_input)
            self.cursor.execute(delete_query)
        else:
            print("Invalid number entered")
    def delete_request(self):
        pass
