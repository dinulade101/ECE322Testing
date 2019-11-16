import hashlib
import sys
from messaging.message import Message


class Member:

    def __init__(self, email, pwd, cursor):
        self.cursor = cursor
        self.email = email
        if not self.login(pwd):
            self.logout()

    @staticmethod
    def signup(email, name, phone, pwd, cursor):
        cursor.execute("INSERT INTO members VALUES (?, ?, ?, ?)",
                       (email, name, phone, pwd))
        return Member(email, pwd, cursor)

    @staticmethod
    def checkIfExists(cursor, email):
        cursor.execute(
            "SELECT COUNT(*) FROM members WHERE email=:email", {"email": email})
        if cursor.fetchone()[0] != 0:
            return True
        return False

    def login(self, pwd):
        self.cursor.execute("SELECT pwd FROM members WHERE email=:email", {
                            "email": self.email})
        result = self.cursor.fetchone()
        if result == None or result[0] != pwd:
            return False
        return True

    def logout(self):
        self.email = None
        self.cursor = None

    def isLoggedIn(self):
        return self.email is not None

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
