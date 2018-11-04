from command.command import Command
from book_rides.offer_ride import OfferRide

class OfferRideCommand(Command):
    def __init__(self, email, cursor):
        super().__init__(cursor)
        self.user = email
        self.ofr = OfferRide(email, cursor)

    def menu(self):
        print('To go back to main menu at any time, enter :menu: in your query\nPress Ctrl + C to quit')

        date = input("Enter a date for this ride (DD/MM/YYYY): ")
        if date == ':menu:':
            return
        while not OfferRideCommand.validateDate(date):
            date = input("Invalid format, enter a date for this value (DD/MM/YYYY): ")
            if date == ':menu:':
                return

        nso = input("Enter the number of seats offered: ")
        if nso == ':menu:':
            return
        while not nso.isdigit():
            nso = input('Invalid input for number of seats, enter a positive number: ')

        ppc = input("Enter the price per seat: ")
        if ppc == ':menu:':
            return
        while not ppc.isdigit():
            ppc = input('Invalid input for price per seat, enter a positive number: ')

        lugDesc = input("Provide luggage description here (only first 10 chars accepted): ")
        if lugDesc == ':menu:':
            return
        lugDesc = lugDesc if len(lugDesc) <= 10 else lugDesc[0:10]

        # TODO
        src = input("Provide a source location keyword: ")
        if src == ':menu:':
            return

        dst = input("Provide a destination location keyword: ")
        if dst == ':menu:':
            return
        # DOTO

        cno = input("Do you want to add your car for this ride (y/n)?: ")
        if cno == ':menu:':
            return
        while not cno.lower() in ['y', 'n']:
            cno = input("Invalid option, do you want to add your car for this ride (y/n)?: ")
            if cno == ':menu:':
                return
        while not self.ofr.checkIfCnoExists(cno):
            cno = input("Car number provided not found! Enter 'n' to exit or provide a different number: ")
            if cno == ':menu:':
                return
            if cno.lower() == 'n':
                break



        pass

    @staticmethod
    def validateDate(date):
        pass
