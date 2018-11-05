from command.command import Command
from book_rides.offer_ride import OfferRide
from datetime import datetime
import re

class OfferRideCommand(Command):
    def __init__(self, email, cursor):
        super().__init__(cursor)
        self.user = email
        self.ofr = OfferRide(email, cursor)

    def menu(self):
        print('To go back to main menu at any time, press Ctrl + C')

        date = input("Enter a date for this ride (YYYY-MM-DD): ")
        while not OfferRideCommand.validateDate(date):
            date = input("Invalid format, enter a date for this value (YYYY-MM-DD): ")
        dateArr = date.split("-")
        date = datetime(int(dateArr[0]), int(dateArr[1]), int(dateArr[2]))

        nso = input("Enter the number of seats offered: ")
        while not nso.isdigit():
            nso = input('Invalid input for number of seats, enter a positive number: ')

        ppc = input("Enter the price per seat: ")
        while not ppc.isdigit():
            ppc = input('Invalid input for price per seat, enter a positive number: ')

        lugDesc = input("Provide luggage description here (only first 10 chars accepted): ")
        lugDesc = lugDesc if len(lugDesc) <= 10 else lugDesc[0:10]

        src = input("Provide a source location keyword: ")
        locs = self.ofr.findLocations(src)
        while len(locs) == 0:
            src = input('No matching locations found! Enter another keyword: ')
            locs = self.ofr.findLocations(src)
        src = self.ofr.getLocationFrom(locs)

        dst = input("Provide a destination location keyword: ")
        locs = self.ofr.findLocations(dst)
        while len(locs) == 0:
            dst = input('No matching locations found! Enter another keyword: ')
            locs = self.ofr.findLocations(dst)
        src = self.ofr.getLocationFrom(locs)

        cno = input("Do you want to add your car for this ride (y/n)?: ")
        while not cno.lower() in ['y', 'n']:
            cno = input("Invalid option, do you want to add your car for this ride (y/n)?: ")
        if cno == 'y':
            cno = input("Enter a car number to associate with this ride: ")
            while not self.ofr.checkIfCnoExists(cno):
                cno = input("Car number provided not found! Enter 'n' to exit or provide a different number: ")
                if cno.lower() == 'n':
                    cno = None
                    break

        enroutes = []
        enr = 'y'
        while enr == 'y':
            enr = input("Do you want to add an/another enroute location for this ride (y/n)?: ")
            if enr.lower() not in ['y', 'n']:
                enr = 'y'
                print('Invalid Option!')
                continue
            if enr == 'n':
                break
            enrCode = input("Provide an enrote location keyword: ")
            locs = self.ofr.findLocations(enrCode)
            while len(locs) == 0:
                enrCode = input('No matching locations found! Enter another keyword: ')
                locs = self.ofr.findLocations(enrCode)
            enrCode = self.ofr.getLocationFrom(locs)
            enroutes.append(enrCode)

        self.ofr.newOffer(date, nso, ppc, lugDesc, src, dst, cno, enroutes)

    @staticmethod
    def validateDate(date):
        if re.match("^(\d){4}-(0\d|1[0-2])-([0-2]\d|3[0-1])$", date):
            return True
        return False
