
class Message:

    def __init__(self, cursor):
        self.cursor = cursor

    def new(self, sndr, rcvr, content, rno):
        self.cursor.execute("INSERT INTO inbox VALUES (:rcvr, datetime('now'), :sndr, :content, :rno, 'n')", {'rcvr':rcvr, 'sndr':sndr, 'content':content, 'rno':rno})

    def unseen(self, user):
        self.cursor.execute("SELECT * FROM inbox WHERE email=:email AND seen='n' ORDER BY msgTimestamp DESC", {"email":user})
        return self.cursor.fetchall()

    def markRead(self, user):
        self.cursor.execute("UPDATE inbox SET seen='y' WHERE email=:email AND seen='n'", {"email":user})
