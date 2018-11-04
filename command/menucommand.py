import sys
from command.command import Command
from command.offerRideCommand import OfferRideCommand

class MenuCommand(Command):
    def __init__(self, email, cursor):
        super().__init__(cursor)
        self.user = email

    def menu(self):
        opt = input('''Select option!\n
        o/O) Offer ride\n
        s/S) Show rides\n
        b/B) Show your bookings\n
        r/R) Make a ride request\n
        v/V) View your ride requests\n
        l/L) Logout\n
        quit) Quit\n''')

        opt = opt.lower()
        if opt == 'o':
            OfferRideCommand(self.user, self.cursor).menu()
        elif opt == 's':
            pass
        elif opt == 'b':
            pass
        elif opt == 'r':
            pass
        elif opt == 'v':
            pass
        elif opt == 'l':
            return False
        elif opt == 'quit':
            sys.exit(0)
        else:
            print('Invalid option!')
            return self.menu()
        return True
