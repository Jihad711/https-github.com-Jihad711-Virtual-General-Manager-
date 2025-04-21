import unittest
from main import app

class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_command(self):
        response = self.app.post('/command', json={"command": "مرحباً"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("response", response.json)

if __name__ == "__main__":
    unittest.main()
