import unittest
import os
from  src.user_manager import add_user, update_user_field, delete_user, show_data, find_data
from src.file_handler import save_update, load_users

class TestUserManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.filename = "test_users.json"
        cls.test_user = {
            "id": 1,
            "name": "Test User",
            "email": "test@example.com",
            "birth_date": "2000-01-01"
        }
        save_update([cls.test_user], cls.filename)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.filename):
            os.remove(cls.filename)

    def test_add_user(self):
        add_user(self.filename)
        users = load_users(self.filename)
        self.assertIn(self.test_user, users)

    def test_update_user_field(self):
        update_user_field("id", 1, 2, self.filename)
        users = load_users(self.filename)
        self.assertEqual(users[0]["id"], 2)

    def test_delete_user(self):
        delete_user(2, self.filename)
        users = load_users(self.filename)
        self.assertNotIn(self.test_user, users)

    def test_show_data(self):
        output = show_data("id", 1, self.filename)
        self.assertIn("Test User", output)

    def test_find_data(self):
        users = load_users(self.filename)
        result = find_data("id", 1, users)
        self.assertTrue(result)
        result = find_data("id", "nonexistent", users)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
