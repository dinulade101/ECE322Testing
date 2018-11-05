from messaging.message import Message 

class SearchRequests:
    def __init__(self, cursor, email):
        self.requests = []
        self.requests_dict = dict()
        self.email = email
        self.cursor = cursor
        self.location = ""
    def find_requests_by_location(self, location):
        self.cursor.execute('''SELECT r.*
        FROM requests r, locations l
        WHERE lower(l.lcode) = r.pickup
        AND (lower(l.lcode) = :location
        OR lower(l.city) = :location
        ) COLLATE NOCASE
        ''', {'email': self.email.lower(), 'location': location.lower()})

        self.requests = self.cursor.fetchall()
        self.location = location
        if (len(self.requests) > 0):
            print('')
            for request in self.requests:
                self.requests_dict[request[0]] = request[1:]
            self.display_results_location(0)
        else:
            print("No results found for location, try again.")
            location = input("Please enter a lcode or city name: ")
            self.find_requests_by_location(location)
        

    def find_requests(self):
        self.cursor.execute('''SELECT r.*
        FROM requests r, locations l
        WHERE l.lcode = r.pickup
        AND r.email = :email
        ''', {'email': self.email})
        self.requests = self.cursor.fetchall()
<<<<<<< HEAD
        if (len(self.requests) > 0):
            print('')
            for request in self.requests:
                self.requests_dict[request[0]] = request[1:]
            self.display_results(0)
        else:
            print("No results found for you. Press Ctrl + C return to main menu.")
    
=======

>>>>>>> c9d884d3f7bc8afcad676ee0496cb67057db85ee
    def format_request(self, ride):
        print("The ride request number is: "+ str(ride[0]))
        print("Email: "+ str(ride[1]))
        print("Ride date: "+ str(ride[2]))
        print("Pickup location: "+ str(ride[3]))
        print("Dropoff location: "+ str(ride[4]))
        print("Amount: "+ str(ride[5]))
        print('')


    def display_results(self, page_num):
        page = self.requests[page_num*5: min(page_num*5+5, len(self.requests))]
        for ride in page:
            print(str(ride[0]) + '.', end='')
            self.format_request(ride)
        if (page_num*5+5 < len(self.requests)):
            user_input = input("To delete a request, please enter the request number. To see more requests more requests enter (y/n): ")
            if (user_input == 'y'):
                self.display_results(page_num+1)
                return
        else:
            user_input = input("To delete a request, please enter the request number: ")
        if user_input.isdigit():
            self.delete_request(user_input)
        else:
            print("Invalid input entered")
            self.display_results(0)

    def display_results_location(self, page_num):
        page = self.requests[page_num*5: min(page_num*5+5, len(self.requests))]
        for ride in page:
            print(str(ride[0]) + '.', end='')
            self.format_request(ride)
        if (page_num*5+5 < len(self.requests)):
            user_input = input("To message the poster of a request, please enter the reqest number. To see more requests enter 'y' : ")
            if (user_input == 'y'):
                self.display_results_location(page_num+1)
                return
        else:
            user_input = input("To message the poster of a request, please enter the reqest number : ")
        if user_input.isdigit():
            self.message_member(user_input)
        else:
            print("Invalid input entered")
            next = input("Press any key to try again. or, press Ctrl + C to return to main menu.")
            if next:
                self.find_requests_by_location(self.location)              

    def message_member(self, user_input):
        if (int(user_input) in self.requests_dict.keys()):
            handler = Message(self.cursor)
            self.cursor.execute("SELECT email FROM requests WHERE rid = :user_input", {'user_input': user_input})
            email = self.cursor.fetchone()[0]

            message_body = input("Please enter the message you want to send " + email + "\n")

            self.cursor.execute("INSERT INTO inbox VALUES (:rcvr, datetime('now'), :sndr, :content, :rno, 'N')", {'rcvr':self.email, 'sndr':email, 'content':message_body, 'rno':'NULL'})
            print("Successfully sent " + email + " with message: \n"+message_body)
            self.find_requests_by_location(self.location)
            #handler.new(self.email, email, message_body, 'NULL')
        else:
            user_input = input("Invalid entry. Please enter a rid again: ")
            self.message_member(user_input)


    def delete_request(self, user_input):
        if (user_input.isdigit() and int(user_input) in self.requests_dict.keys()):
            print("Deleted the following request with rid: " + user_input + '\n')
            self.cursor.execute("DELETE FROM requests WHERE rid = :rid", {'rid': user_input})
            self.find_requests()
        else:
            user_input = input("Invalid entry. Please enter a rid again: ")
            self.delete_request(user_input)


