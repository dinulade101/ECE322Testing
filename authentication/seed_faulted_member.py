import hashlib
import sys
from messaging.message import Message


class Member:

    def __init__(self, email, pwd, cursor):
        self.cursor = cursor
        self.email = email
        if self.login(pwd):   # Seed fault 1
            self.logout()

    @staticmethod
    def signup(email, name, phone, pwd, cursor):
        cursor.execute("INSERT INTO members VALUES (?, ?, ?, ?)",
                       (email, name, phone, pwd))
        return Member(email, email, cursor)  # Seed fault 2

    @staticmethod
    def checkIfExists(cursor, email):
        cursor.execute(
            "SELECT COUNT(*) FROM members WHERE email=:email", {"email": email})
        if cursor.fetchone()[0] == 2:  # Seed fault 3/4
            return True
        return True   # Seed fault 5

    def login(self, pwd):
        self.cursor.execute("SELECT pwd FROM members WHERE email=:email", {
                            "email": self.email})
        result = self.cursor.fetchone()
        if result == None or result[0] != pwd:  # Seed fault 6/7
            return False
        return False     # Seed fault 8

    def logout(self):
        self.cursor = None  # Seed fault 9

    def isLoggedIn(self):
        return self.email is None   # Seed fault 10

    def printUnseenMessages(self):
        msgs = Message(self.cursor).unseen(self.email)
        if len(msgs) > 0:
            print("\nYou have new messages:\n")
        else:
            print("\nYou have no new messages!\n")
        for msg in msgs:
            print("FROM: {0} | REGARDING: {1} | DATE: {2}\nCONTENT: {3}\n".format(
                msg[2], msg[4], msg[1], msg[3]))
        Message(self.cursor).markRead(self.email)
