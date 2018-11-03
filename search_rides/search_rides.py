import sqlite3

class SearchRides:
    def __init__(self, cursor):
        self.cursor = cursor
        self.rides = []
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
        AND c.cno = r.cno
        AND ('''

        for index, word in enumerate(key_words):
            if (index != 0):
                search_query += 'OR '
            search_query += '''l1.lcode LIKE '%{key_word}%'   
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
            '''.format(key_word = word)

        search_query_no_enroute = '''
        SELECT r.*, c.*
        FROM rides r, locations l1, locations l2, cars c
        WHERE l1.lcode = r.src
        AND l2.lcode = r.dst
        AND c.cno = r.cno
        AND ('''

        for index, word in enumerate(key_words):
            if (index != 0):
                search_query_no_enroute += 'OR '
            search_query_no_enroute += '''l1.lcode LIKE '%{key_word}%'   
            OR l1.city LIKE '%{key_word}%' 
            OR l1.prov LIKE '%{key_word}%'  
            OR l1.address LIKE '%{key_word}%' 
            OR l2.lcode LIKE '%{key_word}%'   
            OR l2.city LIKE '%{key_word}%' 
            OR l2.prov LIKE '%{key_word}%'  
            OR l2.address LIKE '%{key_word}%' 
            '''.format(key_word = word)


        search_query += ') UNION' + search_query_no_enroute + ') COLLATE NOCASE'

        self.cursor.execute(search_query)
        self.rides = self.cursor.fetchall()


    def display_rides(self, page_num):
        """
        Displays rides stored in self.rides
        Must run find_rides() prior to calling display_rides()
        :param page_num: specifies which page of rides to be shown (5 rides per page)
        :returns: None 
        """
        #check if page num is valid
        page = self.rides[page_num*5: page_num*5+5]
        for i, ride in enumerate(page):
            print(str(page_num*5+i+1) + '.', end='')
            print(ride)
        if (page_num*5+5 < len(self.rides)):
            user_input = input("See more rides (y/n)?")
            if (user_input == 'y'):
                self.display_rides(page_num+1)
            

        


        


    