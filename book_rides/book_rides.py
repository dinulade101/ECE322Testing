import sqlite3

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
            user_input = input("See more rides (y/n)?")
            if (user_input == 'y'):
                self.display_rides(page_num+1)

    def find_seats_remaining(self, rno):
        query = '''
        SELECT r.seats-COUNT(b.bno) FROM rides r, bookings b 
        WHERE r.rno = {rno}
        AND b.rno = {rno}
        '''.format(rno = rno)

        self.cursor.execute(query)
        rows = self.cursor.fetchone()
        return int(rows[0])
    
    def book_ride(self, member, rno):
        pass
    
    

