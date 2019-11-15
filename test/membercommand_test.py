import unittest
from unittest.mock import patch
from command import membercommand

class TestSum(unittest.TestCase):
    @patch('sqlite3.Cursor')
    def testValidateEmail(self, mock_sql_cursor):
        email = "asdf^gmail.com"
        memberCommand = membercommand.MemberCommand(mock_sql_cursor)
        self.assertFalse(memberCommand.validateEmail(email))
        
if __name__  == "main":
    # with unittest.mock.patch('sys.argv', ['prj-tables.sql']):
    #     membercommand.main()

    unittest.main()