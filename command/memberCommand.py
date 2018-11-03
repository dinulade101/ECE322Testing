import sqlite3
import re
from command.command import Command
from authentication.member import Member

class MemberCommand(Command):
    def __init__(self, cursor):
        super().__init__(cursor)

    def user(self):
        member = None

        opt = input('''Welcome to rideshare!\n
        l/L) To Login\n
        s/S) To Signup\n''')

        if opt.lower() == 'l':
            email = input('Enter your email associated with rideshare: ')
        elif opt.lower() == 's':
            email = input('Enter an email to register with rideshare: ')
        else:
            print('Invalid option')
            return user()

        return member

    def validateEmail(self, email):
        if re.match("^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$" ,email):
            return True
        return False

    def validateName(self, name):
        if re.match(r"" ,name):
            return True
        return False

    def validatePhone(self, phone):
        if re.match(r"^\d{3}-\d{3}-\d{4}$" ,phone):
            return True
        return False
