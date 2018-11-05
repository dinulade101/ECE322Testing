from command.command import Command
from command.cancelBookingCommand import CancelBookingCommand


class bookingCommand(Command):

    def __init__(self, cursor, email):
        super().__init__(cursor)
        self.email = email
