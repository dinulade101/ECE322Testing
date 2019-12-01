import unittest
from unittest.mock import patch
from unittest.mock import Mock
from book_rides.book_rides import BookRides
from authentication.member import Member
from mockito import when, mock, ANY, verify
from io import StringIO
 
EMAIL = "test@test.com"
PASSWORD = "password123"
INVALID_EMAIL = 'invalid@invalid.com'
INVALID_PASSWORD = "123"

class BookRidesTest(unittest.TestCase):
    @patch('sqlite3.Cursor')
    @patch("sys.stdin", StringIO("a\n1\nfailEmail\npassEmail\nfailPickup\npassPickup\nfailDropoff\npassDropoff\nfailCost\n1\nfailSeats\n8\nn\na\n6\ny\n"))
    def testBranchCoverage(self, mock_sql_cursor):     
        mock_sql_cursor = Mock()
       
        bookrides = BookRides(mock_sql_cursor, None)
        when(bookrides).verify_email("failEmail").thenReturn(False)
        when(bookrides).verify_email("passEmail").thenReturn(True)

        when(bookrides).verify_location("failPickup").thenReturn(False)
        when(bookrides).verify_location("passPickup").thenReturn(True)

        when(bookrides).verify_location("failDropoff").thenReturn(False)
        when(bookrides).verify_location("passDropoff").thenReturn(True)

        when(bookrides).generate_bno().thenReturn(2)
        
        bookrides.rides_dict[1] = [2]
        self.assertTrue(bookrides.book_ride())


    @patch('sqlite3.Cursor')
    def testVerifyLocation(self, mock_sql_cursor):     
        mock_sql_cursor = Mock()
       
        bookrides = BookRides(mock_sql_cursor, None)
        
        mock_sql_cursor.fetchone.return_value = [-1]
        self.assertFalse(bookrides.verify_location(""))

        mock_sql_cursor.fetchone.return_value = [1]
        self.assertTrue(bookrides.verify_location(""))


    @patch('sqlite3.Cursor')
    def testVerifyRno(self, mock_sql_cursor):     
        mock_sql_cursor = Mock()
       
        bookrides = BookRides(mock_sql_cursor, None)
        
        mock_sql_cursor.fetchone.return_value = [-1]
        self.assertFalse(bookrides.verify_rno(2))

        mock_sql_cursor.fetchone.return_value = [1]
        self.assertTrue(bookrides.verify_rno(2))

    
    @patch('sqlite3.Cursor')
    def testVerifyEmail(self, mock_sql_cursor):     
        mock_sql_cursor = Mock()
       
        bookrides = BookRides(mock_sql_cursor, None)
        
        mock_sql_cursor.fetchone.return_value = [-1]
        self.assertFalse(bookrides.verify_email(""))

        mock_sql_cursor.fetchone.return_value = [1]
        self.assertTrue(bookrides.verify_email(""))


    @patch('sqlite3.Cursor')
    def testGenerateBno(self, mock_sql_cursor):     
        mock_sql_cursor = Mock()
       
        bookrides = BookRides(mock_sql_cursor, None)
        
        bno = 1
        mock_sql_cursor.fetchone.return_value = [bno]
        self.assertEqual(bookrides.generate_bno(), bno+1)


    @patch('sqlite3.Cursor')
    @patch("sys.stdin", StringIO("c\nb\na\n1\nfailEmail\npassEmail\nfailPickup\npassPickup\nfailDropoff\npassDropoff\nfailCost\n1\nfailSeats\n8\nn\na\n6\ny\n"))
    def testDisplayRidesStatement(self, mock_sql_cursor):
        mock_sql_cursor = Mock()
       
        bookrides = BookRides(mock_sql_cursor, None)
        bookrides.rides = [(1,2,3,4,5,6,7,3,4,5,2,3),(2,3,4,5,3,4,5,6,7,8,2,3),(3,4,5,3,4,5,6,7,2,3,8,9),(4,5,2,33,4,5,6,7,8,9,10),(5,6,3,4,5,2,3,7,8,9,10,11),(3,4,5,6,2,3,7,8,9,10,11,12)]
        when(bookrides).verify_email("failEmail").thenReturn(False)
        when(bookrides).verify_email("passEmail").thenReturn(True)

        when(bookrides).verify_location("failPickup").thenReturn(False)
        when(bookrides).verify_location("passPickup").thenReturn(True)

        when(bookrides).verify_location("failDropoff").thenReturn(False)
        when(bookrides).verify_location("passDropoff").thenReturn(True)

        when(bookrides).generate_bno().thenReturn(2)
        
        bookrides.rides_dict[1] = [2]
        actual = bookrides.display_rides(0)
        self.assertTrue(actual)

    @patch('sqlite3.Cursor')
    @patch("sys.stdin", StringIO("c\ny\nc\nb\na\n1\nfailEmail\npassEmail\nfailPickup\npassPickup\nfailDropoff\npassDropoff\nfailCost\n1\nfailSeats\n8\nn\na\n6\ny\n"))
    def testDisplayRidesStatementRecursiveCall(self, mock_sql_cursor):
        mock_sql_cursor = Mock()
       
        bookrides = BookRides(mock_sql_cursor, None)
        bookrides.rides = [(1,2,3,4,5,6,7,3,4,5,2,3),(2,3,4,5,3,4,5,6,7,8,2,3),(3,4,5,3,4,5,6,7,2,3,8,9),(4,5,2,33,4,5,6,7,8,9,10),(5,6,3,4,5,2,3,7,8,9,10,11),(3,4,5,6,2,3,7,8,9,10,11,12)]
        when(bookrides).verify_email("failEmail").thenReturn(False)
        when(bookrides).verify_email("passEmail").thenReturn(True)

        when(bookrides).verify_location("failPickup").thenReturn(False)
        when(bookrides).verify_location("passPickup").thenReturn(True)

        when(bookrides).verify_location("failDropoff").thenReturn(False)
        when(bookrides).verify_location("passDropoff").thenReturn(True)

        when(bookrides).generate_bno().thenReturn(2)
        
        bookrides.rides_dict[1] = [2]
        actual = bookrides.display_rides(0)
        self.assertTrue(actual)

    @patch('sqlite3.Cursor')
    @patch("sys.stdin", StringIO(""))
    def testDisplayRidesBranch(self, mock_sql_cursor):
        mock_sql_cursor = Mock()
       
        bookrides = BookRides(mock_sql_cursor, None)
        bookrides.rides = [(1,2,3,4,5,6,7,3,4,5,2,3),(2,3,4,5,3,4,5,6,7,8,2,3),(3,4,5,3,4,5,6,7,2,3,8,9),(4,5,2,33,4,5,6,7,8,9,10),(5,6,3,4,5,2,3,7,8,9,10,11),(3,4,5,6,2,3,7,8,9,10,11,12)]
        when(bookrides).book_ride().thenReturn()
        x = bookrides.display_rides(0)
        self.assertTrue(x, True)

if __name__ == "main":
    unittest.main()


def test(x):
    if x < 2:
        x = 5
    return x