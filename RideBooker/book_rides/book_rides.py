import sqlite3
from messaging.message import Message

class BookRides:
    def __init__(self, cursor, user):
        self.cursor = cursor
        self.rides = []
        self.rides_dict = dict()
        self.user = user

    def menu(self):
        self.find_rides(self.user)
        print('\nYour Rides: \n')
        self.display_rides(0)

    def find_rides(self, driver):
        self.cursor.execute('''
        SELECT r.rno, r.price, r.rdate, r.seats, r.lugDesc, r.src, r.dst, r.driver, r.cno, r.seats-IFNULL(SUM(b.seats),0)
        FROM rides r
        LEFT JOIN bookings b
        ON r.rno = b.rno
        WHERE driver = :driver
        GROUP BY r.rno, r.price, r.rdate, r.seats, r.lugDesc, r.src, r.dst, r.driver, r.cno
        ''', {'driver': driver})
        self.rides = self.cursor.fetchall()

        # create rides dictionary for quick access
        for ride in self.rides:
            self.rides_dict[ride[0]] = ride[1:]

    def display_rides(self, page_num):
        page = self.rides[page_num*5: min(page_num*5+5, len(self.rides))]
        for ride in page:
            print('''Ride Number: {0} | Price: {1} | Date: {2} | Seats: {3} | Source: {4} | Destination: {5} |
            Luggage Description: {6} | Car Number: {7} | Available Seats: {8}'''.format(ride[0], ride[1], ride[2], ride[3],
             ride[5], ride[6], ride[4], ride[8], ride[9]))
        if (page_num*5+5 < len(self.rides)):
            user_input = input("\nTo book a member on a ride, please enter 'b/B'. To see more rides, please enter 'y/Y'. To exit to main menu, press ctrl + C: ").lower()
            while user_input not in ['b', 'y']:
                user_input = input('Invalid input, select from the options given: ')
            if (user_input == 'y'):
                self.display_rides(page_num+1)
            if (user_input == 'b'):
                self.book_ride()
        else:
            user_input = input("\nTo book a member on a ride, please enter 'b/B'. To exit to main menu, press ctrl + C: ")
            while user_input not in ['b']:
                user_input = input('Invalid input, select from the options given: ').lower()
            if (user_input == 'b'):
                self.book_ride()


    def generate_bno(self):
        query = "SELECT MAX(bno) FROM bookings"
        self.cursor.execute(query)
        max_bno = self.cursor.fetchone()
        return int(max_bno[0])+1

    def verify_email(self, member):
        self.cursor.execute("SELECT COUNT(email) FROM members WHERE email = :email", {'email':member})
        result = self.cursor.fetchone()
        if (int(result[0]) > 0):
            return True
        else:
            return False

    def verify_rno(self, rno):
        self.cursor.execute("SELECT COUNT(rno) FROM rides WHERE rno = :rno AND driver=:email", {'rno': rno, 'email':self.user})
        result = self.cursor.fetchone()
        if (int(result[0]) > 0):
            return True
        else:
            return False

    def verify_location(self, location):
        self.cursor.execute("SELECT COUNT(lcode) FROM locations WHERE lcode = :lcode", {'lcode': location})
        result = self.cursor.fetchone()
        if (int(result[0]) > 0):
            return True
        else:
            return False

    def notify_member(member, rno, bno, cost, seats, pickup, dropoff):
        # tell other member that they are booked on the ride
        pass

    def book_ride(self):

        rno = input("Please enter a ride number: ")

        while (not rno.isdigit() or not (int(rno) in self.rides_dict.keys())):
            rno = input("Please enter a valid ride number from the rides displayed!: ")

        member = input("Please enter the email of the member you want to book on the ride: ")
        while (not self.verify_email(member)):
            member = input("Please enter a valid member email: ")

        pickup = input("Please enter pick up location code: ")
        while (not self.verify_location(pickup)):
            pickup = input("Please enter a valid pickup location code: ")

        dropoff = input("Please enter drop off location code: ")
        while (not self.verify_location(dropoff)):
            dropoff = input("Please enter a valid dropoff location code: ")

        cost = input("Please enter the cost for ride: ")
        while not cost.isdigit():
            cost = input("Please enter a valid cost: ")

        seats = input("Please enter the number of seats for ride: ")
        while not seats.isdigit():
            seats = input("Please enter a valid number for seats: ")

        while (int(seats) > self.rides_dict[int(rno)][-1]):
            overbook = input("Warning: the ride is being overbooked, are you sure you want to continue (y/n): ")
            if overbook == 'y':
                break
            else:
                seats = input("Please enter a valid number for seats: ")
                while not seats.isdigit():
                    seats = input("Please enter a valid number for seats: ")

        # get unique booking number
        bno = self.generate_bno()

        self.cursor.execute('''INSERT INTO bookings VALUES (:bno, :member, :rno, :cost, :seats, :pickup, :dropoff)
                            ''', {'bno': bno, 'member': member, 'rno': rno, 'cost': cost, 'seats': seats, 'pickup': pickup, 'dropoff': dropoff})

        msg = '''Hi {0}, you've been booked on a ride (ride no: {1}).
        Your booking reference number is {2}. You have booked {3} seats at ${4} per seat.
        Your pickup location is {5} and dropoff is {6}'''.format(member, rno, bno, seats, cost, pickup, dropoff)

        Message(self.cursor).new(self.user, member, msg ,rno)
        print("Ride successfully booked, message sent to the user!")
