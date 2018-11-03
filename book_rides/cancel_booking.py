import sqlite3

class CancelBooking:

    def __init__(self, cursor):
        #assume cursor is already setup
        self.cursor = cursor

    def get_member_bookings(self, m_email):
        self.cursor.execute('''
            SELECT b.bno, b.email, b.rno, b.cost, b.seats
            FROM bookings b, rides r
            WHERE b.rno = r.rno
            AND r.driver = ?
         ''', (m_email,))
        return self.cursor.fetchall()

    def cancel_booking(self, m_email, bno):
        '''
        Call this function to cancel the booking
        :param m_email: The email of the booking driver
        :param bno: bno of the booking
        '''
        deleted_email, rno_deleted = self.delete_booking(bno)
        self.message_deleted_user(m_email ,deleted_email, rno_deleted)



    def delete_booking(self, bno):
        '''
        This function deltes the row with the bno
        :param bno: bno of the row to be deleted
        :return: the email of the deleted row
        '''
        self.cursor.execute('''
            SELECT email, rno
            FROM bookings
            WHERE bno = ?
        ''', (bno,))
        deleted_info = self.cursor.fetchall()
        self.cursor.execute('''
            DELETE
            FROM bookings
            WHERE bno = ?
        ''', (bno, ))

        return deleted_info[0]

    def message_deleted_user(self, deleting_user, deleted_user, rno):
        '''
        This sends a message to the user who's booking was canceled.
        Inserts a row into the inboxs
        :param deleting_user: email of the booking driver
        :param deleted_user: email of the member who's booking was canceled
        :param rno: rno of the ride the booking referred to.
        :return: None
        '''
        self.cursor.execute('''
            INSERT INTO inbox
            VALUES ( ?, datetime('now'), ?,
            "Your ride booking has been deleted. Aplogies for the inconvenience.",
            ?, 'n')
        ''', (deleted_user, deleting_user,rno))
        pass
