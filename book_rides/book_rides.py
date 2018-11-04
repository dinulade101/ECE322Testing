import sqlite3

class InvalidRNOError(error):
    pass
class InvalidMemberError(error):
    pass
class InvalidLocationError(error):
    pass


class BookRides:
    def __init__(self, cursor):
        self.cursor = cursor
        self.rides = []
    def find_rides(self, driver):
        query = '''
        SELECT r.rno, r.price, r.rdate, r.seats, r.lugDesc, r.src, r.dst, r.driver, r.cno, r.seats-COUNT(b.bno) 
        FROM rides r, bookings b
        WHERE driver = '{driver}'
        AND r.rno = b.bno 
        GROUP BY r.rno, r.price, r.rdate, r.seats, r.lugDesc, r.src, r.dst, r.driver, r.cno
        '''.format(driver = driver)

        self.cursor.execute(query)
        self.rides = self.cursor.fetchall()

    def display_rides(self, page_num):
        page = self.rides[page_num*5: min(page_num*5+5, len(self.rides))]
        for i, ride in enumerate(page):
            print(str(page_num*5+i+1) + '.', end='')
            print(ride)
        if (page_num*5+5 < len(self.rides)):
            user_input = input("To book a member on a ride, please enter a ride number. To see more rides, please enter (y/n)?")
            if (user_input == 'y'):
                self.display_rides(page_num+1)
        else:
            user_input = input("To book a member on a ride, please enter a ride number.")
        if user_input.isdigit():
            print("Booking member on ride with rno" + user_input)
        else:
            print("Invalid input entered")

    # def find_seats_remaining(self, rno):
    #     query = '''
    #     SELECT r.seats-COUNT(b.bno) FROM rides r, bookings b 
    #     WHERE r.rno = {rno}
    #     AND b.rno = {rno}
    #     '''.format(rno = rno)

    #     self.cursor.execute(query)
    #     rows = self.cursor.fetchone()
    #     return int(rows[0])

    def generate_bno(self):
        query = "SELECT MAX(bno) FROM bookings"
        self.cursor.execute(query)
        max_bno = self.cursor.fetchone()
        return int(max_bno[0])+1]

    def verify_email(self, member):
        return True

    def verify_rno(self, member):
        return True 
    
    def verify_location(self, location):
        return True 
    
    def book_ride(self, member, rno, cost, seats, pickup, dropoff):

        try:
            rno = input("Please enter a rno: ")
            
            if (not verify_rno(rno)):
                raise InvalidRNOError

            member = input("Please enter the email of the member you want to book on the ride: ")

            if (not verify_email(member)):
                raise InvalidMemberError

            pickup = input("Please enter pick up location code: ")
            dropoff = input("Please enter pick up location code: ")

            if (not (self.verify_location(pickup) AND self.verify_location(dropoff))):
                raise InvalidLocationError
            

            if (not verify_email(member)):
                raise InvalidMemberError

            #get unique booking number
            bno = self.generate_bno()

            query = '''INSERT INTO bookings VALUES ({bno}, {member}, {rno}, {cost}, {seats}, {pickup}, {dropoff})
                    '''.format(bno, member, rno, cost, seats, pickup, dropoff)
        except InvalidRNOError:
            print("Please enter a valid rno") 

        except InvalidMemberError:
            print("Please enter a valid member email")
            self.book_ride()
        except InvalidLocationError:
            print("Please enter a valid pickup and dropoff location code")
            self.book_ride()

    
    

