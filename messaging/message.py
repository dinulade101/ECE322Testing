
class Message:

    def __init__(self, cursor):
        self.cursor = cursor

    def new(self, sndr, rcvr, content, rno):
        self.cursor.execute("INSERT INTO inbox VALUES (:rcvr, datetime('now'), :sndr, :content, :rno, 'N')", {'rcvr':rcvr, 'sndr':sndr, 'content':content, 'rno':rno})
        #self.cursor.execute("SELECT * FROM inbox")
        #query = "INSERT INTO inbox VALUES ('{rcvr}', datetime('now'), '{sndr}', '{content}', {rno}, 'N')".format(rcvr = rcvr, sndr = sndr, content = content, rno = rno)
        #print(query)
        #self.cursor.execute(query)

    def unseen(self, user):
        self.cursor.execute("SELECT * FROM inbox WHERE email=:email AND seen='N' ORDER BY msgTimestamp DESC", {"email":user})
        return self.cursor.fetchall()

    def markRead(self, user):
        self.cursor.execute("UPDATE inbox SET seen='Y' WHERE email=:email AND seen='N'", {"email":user})
