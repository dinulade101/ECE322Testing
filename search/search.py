import sqlite3

class Search:
    def __init__(self, cursor):
        self.cursor = cursor
    def is_key_word_valid(self,word):
        return word
    def return_rides(self, key_words):
        
        search_query = '''
        SELECT * 
        FROM rides r, locations l1, locations l2, locations l3, enroute e
        WHERE l1.lcode = r.src
        AND l2.lcode = r.dst
        AND e.rno = r.rno 
        AND l3.lcode = e.lcode
        AND ('''

        for index, word in enumerate(key_words):
            if (index != 0):
                search_query += 'OR '
            search_query += '''l1.lcode LIKE '%{key_words}%'   
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

        search_query += ').format(key_words = key_words)'

        self.cursor.execute(search_query)
        rows = self.cursor.fetchall()

        return rows
    def display_rides(self, page_num):
        pass


    