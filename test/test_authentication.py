import unittest
from unittest.mock import patch
from unittest.mock import Mock
from authentication.member import Member

EMAIL = "test@test.com"
PASSWORD = "password123"
INVALID_EMAIL = 'invalid@invalid.com'
INVALID_PASSWORD = "123"

# Assumptions: The member class assumes that all data like email
# phone, name and password that are passed to its functions are valid.
# In order to validate the data the membercommand class can be used.


class AuthenticationTest(unittest.TestCase):

    # Unit Tests
    def testCheckIfExists(self):
        mock_sql_cursor = Mock()
        mock_sql_cursor.fetchone.return_value = [1]
        mem = Member(EMAIL, PASSWORD, mock_sql_cursor)

        # Error guessing
        self.assertTrue(mem.checkIfExists(mock_sql_cursor, EMAIL))

        mock_sql_cursor.fetchone.return_value = [0]
        self.assertFalse(mem.checkIfExists(mock_sql_cursor, INVALID_EMAIL))

    def testSignup(self):
        mock_sql_cursor = Mock()
        mock_sql_cursor.fetchone.return_value = [PASSWORD]
        mem = Member.signup(EMAIL, "jim", "111-111-1111",
                            PASSWORD, mock_sql_cursor)
        self.assertEqual(EMAIL, mem.email)

    def testLogin(self):
        mock_sql_cursor = Mock()
        mock_sql_cursor.fetchone.return_value = [PASSWORD]
        mem = Member.signup(EMAIL, "jim", "111-111-1111",
                            PASSWORD, mock_sql_cursor)
        self.assertTrue(mem.login)

    def testValidSignUpLogin(self):
        # Signup a new user
        mock_sql_cursor = Mock()
        mock_sql_cursor.fetchone.return_value = [INVALID_PASSWORD]
        mem = Member(EMAIL, PASSWORD, mock_sql_cursor)
        self.assertFalse(mem.isLoggedIn())

        # Login a new user
        mock_sql_cursor.fetchone.return_value = [PASSWORD]
        new_mem = mem.signup(EMAIL, "jim", "111-111-1111",
                             PASSWORD, mock_sql_cursor)
        self.assertTrue(new_mem.login(PASSWORD))
        self.assertTrue(new_mem.isLoggedIn())
        new_mem.logout()
        self.assertFalse(new_mem.isLoggedIn())

    def testInvalidSignUpLogin(self):
        # Login a user that hasn't signed up
        mock_sql_cursor = Mock()
        mock_sql_cursor.fetchone.return_value = [INVALID_PASSWORD]
        mem = Member(EMAIL, PASSWORD, mock_sql_cursor)
        self.assertFalse(mem.isLoggedIn())

        # Error found: Trying to login a user after initializing with an
        # incorrect password throws an error instead of returning False
        self.assertFalse(mem.login(PASSWORD))
        self.assertFalse(mem.isLoggedIn())


if __name__ == "main":
    unittest.main()
