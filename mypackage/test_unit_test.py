import unittest
from .main import greeting


class TestHello(unittest.TestCase):
    def test_pass_1(self):
        self.assertEqual(greeting(), "Hello Nhat Quan Bui")
        print("Test pass 1 is Ok")

    def test_pass_2(self):
        self.assertTrue(isinstance(greeting(), str))
        print("Test pass 2 is Ok")

    def test_pass_3(self):
        self.assertTrue(len(greeting()) > 0)
        print("Test pass 3 is Ok")

    def test_fail_1(self):
        self.assertEqual(greeting(), "Hello my name")

    def test_fail_2(self):
        self.assertIsNone(greeting())


if __name__ == "__main__":
    unittest.main()
