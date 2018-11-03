import sqlite3

class PostRide:

    def __init__(self, cursor):
        #assume cursor is
        self.cursor = cursor

    def validate_location(self, loc_code):
        """
        Checks if the location code is in the locations db
        :param loc_code: location code that we want to validate
        :returns: boolean value whether or not the location is in the db
        """
        self.cursor.execute('SELECT * FROM locations WHERE lcode = ?;', loc_code)
        return self.cursor.rowcount != 0

    def insert_req(self, values):
        """
        Inserts the request with a unique id
        :param values: key value pair of values to write
        :returns: None
        """
        self.cursor.execute('SELECT MAX(rid) FROM requests;')
        next_id = self.cursor.fetchone()
        print(next_id)
