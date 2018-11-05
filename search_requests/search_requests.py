from messaging.message import Message 

class SearchRequests:
    def __init__(self, cursor, email):
        self.requests = []
        self.email = email
        self.cursor = cursor
    def find_requests_by_location(self, location):
        self.cursor.execute('''SELECT r.*
        FROM requests r, locations l
        WHERE l.lcode = r.pickup
        AND (l.lcode = :location
        OR l.city = :location
        ) COLLATE NOCASE
        ''', {'email': self.email, 'location': location})

        self.requests = self.cursor.fetchall()
        if (len(self.requests) > 0):
            print('')
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

    def display_results_location(self, page_num):
        page = self.requests[page_num*5: min(page_num*5+5, len(self.requests))]
        for ride in page:
            print(str(ride[0]) + '.', end='')
            self.format_request(ride)
        if (page_num*5+5 < len(self.requests)):
            user_input = input("To message the poster of a request, please enter the reqest number. To see more requests more requests enter 'y'. \n To exit to main menu, press Ctrl + C: ")
            if (user_input == 'y'):
                self.display_results(page_num+1)
                return
        else:
            user_input = input("To message the poster of a request, please enter the reqest number. \n To exit to main menu, press Ctrl + C: ")
        if user_input.isdigit():
            self.message_member(user_input)
        else:
            print("Invalid input entered")
            self.display_results_location(0)

    def message_member(self, user_input):
        handler = Message(self.cursor)
        self.cursor.execute("SELECT email FROM requests WHERE rid = :user_input", {'user_input': user_input})
        email = self.cursor.fetchone()[0]

        message_body = input("Please enter the message you want to send " + email + "\n")

        self.cursor.execute("INSERT INTO inbox VALUES (:rcvr, datetime('now'), :sndr, :content, :rno, 'N')", {'rcvr':self.email, 'sndr':email, 'content':message_body, 'rno':'NULL'})
        print("Successfully sent " + email + " with message: \n"+message_body)
        #handler.new(self.email, email, message_body, 'NULL')

    
    def delete_request(self, user_input):
        print("Deleted the following request with rid: " + user_input)
        self.cursor.execute("DELETE FROM requests WHERE rid = :rid", {'rid': user_input})
