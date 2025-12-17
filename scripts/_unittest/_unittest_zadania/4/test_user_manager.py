import unittest
from unittest.mock import patch, Mock
from user_manager import UserManager


class TestUserManager(unittest.TestCase):

    def setUp(self):
        pass  # TODO: Create UserManager instance

    @patch('user_manager.sqlite3.connect')
    def test_create_user_returns_user_id(self, mock_connect):
        """Test that create_user returns the generated user ID."""
        assert False  # TODO: Mock cursor, lastrowid=123, test create_user returns 123

    @patch('user_manager.sqlite3.connect')  
    def test_create_user_executes_correct_sql(self, mock_connect):
        """Test that create_user executes correct SQL with parameters."""
        assert False  # TODO: Mock cursor, test that cursor.execute called with INSERT SQL and ("John", "john@test.com")

    @patch('user_manager.sqlite3.connect')
    def test_get_user_returns_user_dict(self, mock_connect):
        """Test that get_user returns user dict when user exists."""
        assert False  # TODO: Mock cursor, fetchone() return (1, "John", "john@test.com"), test result dict

    @patch('user_manager.sqlite3.connect')
    def test_get_user_returns_none_when_not_found(self, mock_connect):
        """Test that get_user returns None when user not found."""
        assert False  # TODO: Mock cursor, fetchone() return None, test get_user returns None

    @patch('user_manager.sqlite3.connect')
    def test_delete_user_returns_true_when_deleted(self, mock_connect):
        """Test that delete_user returns True when user was deleted."""
        assert False  # TODO: Mock cursor, rowcount = 1, test delete_user returns True

    @patch('user_manager.sqlite3.connect')
    def test_delete_user_returns_false_when_not_found(self, mock_connect):
        """Test that delete_user returns False when user not found."""
        assert False  # TODO: Mock cursor, rowcount = 0, test delete_user returns False

    @patch('user_manager.sqlite3.connect')
    def test_user_exists_returns_true_when_found(self, mock_connect):
        """Test that user_exists returns True when email found."""
        assert False  # TODO: Mock cursor, fetchone() return (1,), test user_exists returns True

    @patch('user_manager.sqlite3.connect')
    def test_user_exists_returns_false_when_not_found(self, mock_connect):
        """Test that user_exists returns False when email not found."""
        assert False  # TODO: Mock fetchone() return (0,), test user_exists returns False


if __name__ == '__main__':
    unittest.main()