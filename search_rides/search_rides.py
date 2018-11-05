import sqlite3
from messaging.message import Message

class SearchRides:
    def __init__(self, cursor, email):
        self.cursor = cursor
        self.rides = []
        self.email = email

    def containsRno(self, rno):
        for ride in self.rides:
            if ride[0] == rno:
                return True
        return False

    def is_key_word_valid(self,word):
        return word

    def find_rides(self, key_words):
        """
        Finds rides that match locations that match the key_words provided
        Stores found rides in self.rides array
        :param key_words: array of 1-3 strings specifying key words locations should be matched to
        :returns: None
        """

        search_query = '''
        SELECT r.*, c.*
        FROM rides r, locations l1, locations l2, locations l3, enroute e, cars c
        WHERE l1.lcode = r.src
        AND l2.lcode = r.dst
        AND e.rno = r.rno
        AND l3.lcode = e.lcode
        AND c.cno = r.cno'''

        for index, word in enumerate(key_words):
            if (index != 0):
                search_query += ''
            search_query += ''' AND (l1.lcode LIKE '%{key_word}%'
            OR l1.city LIKE '%{key_word}%'
            OR l1.prov LIKE '%{key_word}%'
            OR l1.address LIKE '%{key_word}%'
            OR l2.lcode LIKE '%{key_word}%'
            OR l2.city LIKE '%{key_word}%'
            OR l2.prov LIKE '%{key_word}%'
            OR l2.address LIKE '%{key_word}%'
            OR l3.lcode LIKE '%{key_word}%'
            OR l3.city LIKE '%{key_word}%'
            OR l3.prov LIKE '%{key_word}%'
            OR l3.address LIKE '%{key_word}%'
            )'''.format(key_word = word)

        search_query_no_enroute = '''
        SELECT r.*, c.*
        FROM rides r, locations l1, locations l2, cars c
        WHERE l1.lcode = r.src
        AND l2.lcode = r.dst
        AND c.cno = r.cno'''

        for index, word in enumerate(key_words):
            if (index != 0):
                search_query_no_enroute += ''
            search_query_no_enroute += ''' AND (l1.lcode LIKE '%{key_word}%'
            OR l1.city LIKE '%{key_word}%'
            OR l1.prov LIKE '%{key_word}%'
            OR l1.address LIKE '%{key_word}%'
            OR l2.lcode LIKE '%{key_word}%'
            OR l2.city LIKE '%{key_word}%'
            OR l2.prov LIKE '%{key_word}%'
            OR l2.address LIKE '%{key_word}%'
            )'''.format(key_word = word)


        search_query += ' UNION' + search_query_no_enroute + ' COLLATE NOCASE'

        self.cursor.execute(search_query)
        self.rides = self.cursor.fetchall()
        if (len(self.rides) == 0):
            print("No result found for the following keywords. Please try again.")
            self.menu()
            return
        self.display_rides(0)

    def format_ride(self, ride):
        print("The ride number is: "+ str(ride[0]))
        print("Price: "+ str(ride[1]))
        print("Date: "+ str(ride[2]))
        print("Number of Seats: "+ str(ride[3]))
        print("Luggage Description: "+ str(ride[4]))
        print("Start: "+ str(ride[5]))
        print("Destination: "+ str(ride[6]))
        print("Driver: "+ str(ride[7]))
        print("Car Number: "+ str(ride[8]) + '\n')

    def menu(self):
        user_input = input("Please enter 1-3 location key words each seperated by a comma: ").split(',')
        if (len(user_input) > 3 or len(user_input) == 0 or user_input[0] == ''):
            print("Please enter a valid set of key words. Otherwise, to return to main menu press Ctrl + C: ")
            self.menu()
            return
        print(user_input)
        for index in range(len(user_input)):
            user_input[index] = user_input[index].strip()

        self.find_rides(user_input)
        self.display_rides(0)

    def display_rides(self, page_num):
        """
        Displays rides stored in self.rides
        Must run find_rides() prior to calling display_rides()
        :param page_num: specifies which page of rides to be shown (5 rides per page)
        :returns: None
        """
        if page_num == 0:
            print()
        page = self.rides[page_num*5: min(page_num*5+5, len(self.rides))]
        for ride in page:
            print(str(ride[0]) + '.', end='')
            self.format_ride(ride)
        if (page_num*5+5 < len(self.rides)):
            user_input = input("To see more rides enter 'y', To message the poster of a ride, enter the ride number:  ")
            if (user_input == 'y'):
                self.display_rides(page_num+1)
                return
        else:
            user_input = input("To message the poster of a ride, please enter the ride number: ")
        if user_input.isdigit() and self.containsRno(user_input):
            self.message_member(user_input)
        else:
            print("\nInvalid input entered, please select from ride number displayed")
            self.display_rides(0)


    def message_member(self, user_input):
        handler = Message(self.cursor)
        self.cursor.execute("SELECT driver FROM rides WHERE rno = :user_input", {'user_input': user_input})
        email = self.cursor.fetchone()[0]

        message_body = input("Please enter the message you want to send to " + email + "\n")

        print("Successfully sent " + email + " with message: \n"+message_body)
        handler.new(self.email, email, message_body, user_input)
        print('')
