import sqlite3
import re
import sys
import getpass
from command.command import Command
from authentication.member import Member

class MemberCommand(Command):
    def __init__(self, cursor):
        super().__init__(cursor)

    def user(self):
        member = None

        opt = input('''Welcome to rideshare!\n
        l/L) To Login\n
        s/S) To Signup\n
        ctrl + C) Show this menu again\n
        quit) Quit\n''')

        if opt.lower() == 'l':
            email = input('Enter your email associated with rideshare: ')
            while not self.validateEmail(email):
                email = input('Please enter a valid email: ')
            pwd = getpass.getpass('Enter your password: ')

            member = Member(email, pwd, self.cursor)
            if not member.isLoggedIn():
                print('\nInvalid email and password combination!\n')
                return self.user()
            else:
                return member

        elif opt.lower() == 's':
            email = input('Enter an email to register with rideshare: ')
            while not self.validateEmail(email):
                email = input('Please enter a valid email: ')
            if Member.checkIfExists(self.cursor, email):
                print('\nEmail already taken!\n')
                return self.user()
            name = input('Enter a name to register with this email (format: AlphaNumeric, <=20 char): ')
            while not self.validateName(name):
                name = input('Please enter a valid name: ')
            phone = input('Enter your phone number (format: XXX-XXX-XXXX): ')
            while not self.validatePhone(phone):
                phone = input('Please enter a valid number: ')
            pwd = getpass.getpass('Enter a password to associate with this account: ')
            member = Member.signup(email, name, phone, pwd, self.cursor)

        elif opt.lower() == 'quit':
            sys.exit(0)

        else:
            print('Invalid option')
            return self.user()

        return member

    @staticmethod
    def validateEmail(email):
        if re.match("^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$" ,email):
            return True
        return False

    @staticmethod
    def validateName(name):
        if len(name) <= 20 and len(name) > 0:
            return True
        return False

    @staticmethod
    def validatePhone(phone):
        if re.match(r"^\d{3}-\d{3}-\d{4}$" ,phone):
            return True
        return False
