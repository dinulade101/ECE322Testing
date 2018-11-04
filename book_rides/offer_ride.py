import sqlite3

class OfferRide:

    def __init__(self, email, cursor):
        self.user = email
        self.cursor = cursor

    def checkIfCnoExists(self, cno):
        cursor.execute("SELECT COUNT(*) FROM cars WHERE cno=:cno", {"cno":cno})
        if cursor.fetchone()[0] != 0:
            return True
        return False

    def findLocations(self, keyword):
        pass

    def getLocationFrom(self, locs):
        pass
