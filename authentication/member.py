import hashlib
import sys

class Member:

    def __init__(self, email, pwd, cursor):
        self.cursor = cursor
        self.email = email
        if not self.login(pwd):
            self.logout()

    @staticmethod
    def signup(email, name, phone, pwd, cursor):
        cursor.execute("INSERT INTO members VALUES (?, ?, ?, ?)", (email, name, phone, Member.hash(pwd)))
        return Member(email, pwd, cursor)

    @staticmethod
    def hash(pwd):
        return hashlib.sha256(pwd.encode()).hexdigest()

    @staticmethod
    def checkIfExists(cursor, email):
        cursor.execute("SELECT COUNT(*) FROM members WHERE email=:email", {"email":email})
        if cursor.fetchone()[0] != 0:
            return True
        return False

    def login(self, pwd):
        self.cursor.execute("SELECT pwd FROM members WHERE email=:email", {"email":self.email})
        result = self.cursor.fetchone()
        if result == None or result[0] != Member.hash(pwd):
            return False
        return True

    def logout(self):
        self.email = self.cursor = None

    def isLoggedIn(self):
        return self.email is not None
