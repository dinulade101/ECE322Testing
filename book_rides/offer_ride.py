import sqlite3

class OfferRide:

    def __init__(self, email, cursor):
        self.user = email
        self.cursor = cursor
