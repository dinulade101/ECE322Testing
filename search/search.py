import sqlite3

class Search:
    def __init__(self, cursor):
        self.cursor = cursor
        self.rides = []
    def is_key_word_valid(self,word):
        return word
    def return_rides(self, key_words):
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

        search_query += ')'

        print(search_query)



        self.cursor.execute(search_query)
        self.rides = self.cursor.fetchall()

    '''
    display_rides function requires that return_rides be called prior
    page_num index starts at 1 
    '''
    def display_rides(self, page_num):
        page_num -= 1
        #check if page num is valid
        page = self.rides[page_num*5:page_num*5+5]
        for i, ride in enumerate(page):
            print(str(i+1) + '.', end='')
            print(ride)
        


        


    