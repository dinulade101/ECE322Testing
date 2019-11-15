import unittest
from unittest.mock import patch
from command import membercommand


class MemberCommandTest(unittest.TestCase):
    @patch('sqlite3.Cursor')
    def testValidateEmail(self, mock_sql_cursor):
        memberCommand = membercommand.MemberCommand(mock_sql_cursor)

        # Error guessing
        self.assertFalse(memberCommand.validateEmail(""))  # empty input

        # Equivalence classes
        """
            Valid equivalence classes for email address:
                * string including @
                * string consisting of alphanumeric characters
            Invalid equivalence classes for email address:
                * string without '@'
                * string containing special chars like *
        """
        self.assertTrue(memberCommand.validateEmail(
            "asdf@gmail.com"))  # string including '@'
        # string of alpha numeric characters
        self.assertTrue(memberCommand.validateEmail("asdf123@g2mail.com"))

        self.assertFalse(memberCommand.validateEmail(
            "asdf^gmail.com"))  # string without '@'
        # string containing special chars.
        self.assertFalse(memberCommand.validateEmail("asdf*@gmail.com"))

    @patch('sqlite3.Cursor')
    def testValidateName(self, mock_sql_cursor):
        memberCommand = membercommand.MemberCommand(mock_sql_cursor)

        # Error guessing
        self.assertFalse(memberCommand.validateName(""))  # empty input

        # boundary testing where the charater limit is 20:
        self.assertTrue(memberCommand.validateName(
            "Asadnfjsdnfjsdnajfnf"))  # 20 chars
        self.assertFalse(memberCommand.validateName(
            "Asadnfjsdnfjsdnajfnfn"))  # 21 chars

        self.assertTrue(memberCommand.validateName("Bob"))

    @patch('sqlite3.Cursor')
    def testValidatePhoneNumber(self, mock_sql_cursor):
        memberCommand = membercommand.MemberCommand(mock_sql_cursor)

        # Error guessing
        self.assertFalse(memberCommand.validatePhone(""))  # empty input

        # Equivalence classes
        """
            Valid equivalence classes for name:
                * string consisting of 9 numeric characters 
            Invalid equivalence classes for email address:
                * string consisting of non numeric characters 
                * string having less than 9 numbers 
                * string having greater than 9 numbers 
                * numbers not in format (NNN-NNN-NNNN)
        """
        self.assertTrue(memberCommand.validatePhone("403-000-0000")
                        )  # 9 numeric characters in format (NNN-NNN-NNNN)

        self.assertFalse(memberCommand.validatePhone(
            "40a-000-0000"))  # non numeric characters
        self.assertFalse(memberCommand.validatePhone(
            "4-000-0000"))  # less than 9 numbers
        self.assertFalse(memberCommand.validatePhone(
            "403-0001-0000"))  # greater than 9 numbers
        self.assertFalse(memberCommand.validatePhone(
            "40-000-10000"))  # numbers not in format


if __name__ == "main":
    # with unittest.mock.patch('sys.argv', ['prj-tables.sql']):
    #     membercommand.main()

    unittest.main()
