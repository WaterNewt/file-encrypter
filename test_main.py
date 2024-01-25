import unittest
from utils import *
from main import main
from unittest.mock import patch


class TestCLI(unittest.TestCase):
    def test_decrypt(self):
        self.assertEqual(decrypt_text(b'gAAAAABllTEUfhs83IeO4gOmeOUjLBWAr2kHDxE4WXEOKTuKQ-iEEEo7lVIKCa0-aZk0l895bRGc8nE8DMMXuOPFXLoc2isZDA==', "test"), b"Hello")
    
    def test_encrypt(self):
        self.assertEqual(decrypt_text(encrypt_text(b"Hello", "test"), "test"), b'Hello')


class TestMain(unittest.TestCase):
    path_to_image_original = 'tests/fixtures/test_main_original.png'
    path_to_image_original_copy = 'tests/fixtures/test_main_original_copy.png'
    password = 'qwerty123'

    @patch('builtins.print')
    def test_1_valid_input_encrypt(self, mock_print):
        with patch('sys.argv', ['main.py', TestMain.path_to_image_original, '-e', '-p', TestMain.password]):
            main()

    @patch('builtins.print')
    def test_2_valid_input_decrypt(self, mock_print):
        with patch('sys.argv', ['main.py', TestMain.path_to_image_original, '-d', '-p', TestMain.password]):
            main()

    def test_data_integrity(self):
        with open(TestMain.path_to_image_original, 'rb') as file:
            text_original = file.read()

        with open(TestMain.path_to_image_original_copy, 'rb') as file:
            text_original_copy = file.read()
        self.assertEqual(text_original, text_original_copy, f"Expected {text_original_copy}, but got {text_original}")


if __name__ == "__main__":
    unittest.main()
