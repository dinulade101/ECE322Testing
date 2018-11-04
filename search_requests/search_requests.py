class SearchRequests:
    def __init__(self, cursor, email):
        self.requests = []
        self.email = email
        self.cursor = cursor
    def find_requests(self, location):
        self.cursor.execute('''SELECT r.*
        FROM requests r, locations l
        WHERE l.lcode = r.pickup
        AND r.email = :email
        AND (l.lcode = :location
        OR l.city = :location
        ) COLLATE NOCASE
        ''', {'email': self.email, 'location': location})

        self.requests = self.cursor.fetchall()

    def find_requests(self):
        self.cursor.execute('''SELECT r.*
        FROM requests r, locations l
        WHERE l.lcode = r.pickup
        AND r.email = :email
        ''', {'email': self.email})
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
                return
        else:
            user_input = input("To delete a request, please enter the reqest number: ")
        if user_input.isdigit():
            print("Deleted the following request with rid: " + user_input)
            self.cursor.execute("DELETE FROM requests WHERE rid = :rid", {'rid': user_input})
        else:
            print("Invalid input entered")
            self.display_results(0)

    def delete_request(self, user_input):
        print("Deleted the following request with rid: " + user_input)
        self.cursor.execute("DELETE FROM requests WHERE rid = :rid", {'rid': user_input})
