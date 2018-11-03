from command.command import Command

class MenuCommand(Command):
    def __init__(self, cursor):
        super().__init__(cursor)

    def menu(self):
        opt = input('''Select option!\n
        o/O) Offer ride\n
        s/S) Show rides\n
        b/B) Show bookings\n
        ctrl + C) Quit\n''')
        pass
