import hashlib
import sys

class Member:

    def __init__(self, email, pwd, cursor):
        self.cursor = cursor
        self.email = email
        if not self.login(pwd):
            self.logout()

    def signup(email, name, phone, pwd):
        if checkIfExists(email):
            return None
        self.cursor.execute("INSERT INTO members VALUES (?, ?, ?, ?)", (email, name, phone, hash(pwd)))
        conn.commit()
        return Member(email, pwd)

    @staticmethod
    def hash(pwd):
        return hashlib.sha256(pwd.encode()).hexdigest()

    def checkIfExists(email):
        self.cursor.execute("SELECT COUNT(*) FROM members WHERE email=:email", {"email":email})
        if self.cursor.fetchone()[0] != 0:
            return True
        return False

    def login(self, pwd):
        self.cursor.execute("SELECT pwd FROM members WHERE email=:email", {"email":self.email})
        if self.cursor.fetchone()[0] != hash(pwd):
            return False
        return True

    def logout(self):
        self.email = self.cursor = None

    def isLoggedIn(self):
        return self.email is not None
