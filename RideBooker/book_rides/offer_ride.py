import sqlite3

class OfferRide:

    def __init__(self, email, cursor):
        self.user = email
        self.cursor = cursor

    def checkIfCnoExists(self, cno):
        self.cursor.execute("SELECT COUNT(*) FROM cars WHERE cno=:cno AND owner=:email", {"cno":cno, "email":self.user})
        if self.cursor.fetchone()[0] != 0:
            return True
        return False

    def findLocations(self, keyword):
        query = '''
        SELECT l.*
        FROM locations l
        WHERE l.lcode LIKE :keyword
        OR l.city LIKE  :keyword
        OR l.prov LIKE :keyword
        OR l.address LIKE :keyword
        COLLATE NOCASE;
        '''
        self.cursor.execute(query, {"keyword": '%' + keyword + '%'})
        return self.cursor.fetchall()

    def getLocationFrom(self, locs):
        print('Your search returned following items:')

        display_index = 0
        selection_index = 0

        while True:
            for i in range(display_index, min(display_index + 5, len(locs))):
                print("{0}) | Location Code: {1} | City: {2} | Province: {3} | Address: {4}".format(i, locs[i][0], locs[i][1], locs[i][2], locs[i][3]))

            print_more = input("Would you like to see more results (y/n)?: ").lower()

            while print_more not in ['y', 'n']:
                print_more = input('Invalid option! Would you like to see more results (y/n)?: ').lower()
            if print_more == 'y':
                if display_index + 5 > len(locs):
                    print('No more matches found!')
                display_index += 5
            else:
                selection_index = input('Select an index from search results: ')
                while not selection_index.isdigit() or int(selection_index) >= len(locs):
                    selection_index = input('Invalid input! Select an index from the results displayed: ')
                break
        return locs[int(selection_index)][0]

    def newOffer(self, date, seats, price, lugDesc, src, dst, cno, enroutes):
        self.cursor.execute("SELECT MAX(rno) FROM rides")
        rno = self.cursor.fetchone()[0] + 1
        self.cursor.execute("INSERT INTO rides VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (rno, price, date, seats, lugDesc, src, dst, self.user, cno))
        for enr in enroutes:
            self.cursor.execute("INSERT INTO enroute VALUES (?, ?)", (rno, enr))
