import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import greet


class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(
            greet("World"),
            "Hello, World from Mohammad Aboulhoda:",
        )


if __name__ == "__main__":
    unittest.main()

