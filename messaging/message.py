
class Message:

    def __init__(self, cursor):
        self.cursor = cursor

    def new(self, sndr, rcvr, content, rno):
        self.cursor.execute("INSERT INTO inbox VALUES (?, datetime('now'), ?, ?, ?, 'N')", (rcvr, sndr, content, rno))

    def unseen(self, user):
        self.cursor.execute("SELECT * FROM inbox WHERE email=:email AND seen='N' ORDER BY msgTimestamp DESC", {"email":user})
        return self.cursor.fetchall()

    def markRead(self, user):
        self.cursor.execute("UPDATE inbox SET seen='Y' WHERE email=:email AND seen='N'", {"email":user})
