from command.command import Command

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
        ctrl + C) Quit\n''')

        opt = opt.lower()
        if opt == 'o':
            pass
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
        else:
            print('Invalid option!')
            return self.menu()
        return True
