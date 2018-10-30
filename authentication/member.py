import hashlib

class Member:

    def __init__(self, email, pwd):
        self.email = email
        if not self.login(pwd):
            self.logout()

    @staticmethod
    def signup(email, name, phone, pwd):
        ## TODO: signup a user and register
        print('Signup succesful!')
        return Member(email, pwd)

    @staticmethod
    def hash(pwd):
        return hashlib.sha256(pwd.encode()).hexdigest()

    @staticmethod
    def checkIfExists(email):
        ## TODO: print email already taken if it exists
        return False

    def login(self, pwd):
        ## TODO: print invalid combination on failed login
        print('Welcome to ride share!')
        return True

    def logout(self):
        self.email = None

    def isLoggedIn(self):
        return self.email is not None
