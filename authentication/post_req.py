import sqlite3


class PostReq:

    def __init__(self, cursor):
        #assume cursor is
        self.cursor = cursor

    def validate_location(self, loc_code):
        """
        Checks if the location code is in the locations db
        :param loc_code: location code that we want to validate
        :returns: boolean value whether or not the location is in the db
        """
        self.cursor.execute('SELECT * FROM locations WHERE lcode = ? COLLATE NOCASE;', (loc_code,))
        return len(self.cursor.fetchall()) != 0
    
    def insert_req(self, values):
        """
        Inserts the request with a unique id
        :param values: key value pair of values to write. Keys are all the same name 
        as the names of requests columns
        :returns: None 
        """
        self.cursor.execute('SELECT MAX(rid) FROM requests;')
        try:
            rid = self.cursor.fetchone()[0] + 1
        except(TypeError):
            rid = 1
        print(rid)
        values['rid'] = rid

        self.cursor.execute('INSERT INTO requests VALUES (:rid, :email, :rdate, :pickup, :dropoff, :amount);',values)


