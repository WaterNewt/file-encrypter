import unittest
import random
import string
import io

from unittest.mock import patch
from utils import generate_key, encrypt_text, decrypt_text, clean_exit


class TestGenerateKey(unittest.TestCase):
    def test_alphanumeric(self):
        result = generate_key('qwerty123')
        expected = b'pEKW7lA7YVt0wzd2vT3Co_67xSnQxwfcGwI18ubYqx8='
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_mixed(self):
        result = generate_key('qwerty123!$@+')
        expected = b'aFL9m9eTYcpG6XD36wH0E7J-1wr4PrkEKPmFg3_B3mA='
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")


class TestEncryptText(unittest.TestCase):
    def test_comparison_by_type(self):
        path_to_image = 'tests/fixtures/test_encrypt_text.png'
        with open(path_to_image, 'rb') as file:
            text = file.read()
        result = encrypt_text(text, 'qwerty123')
        expected = bytes
        self.assertIsInstance(result, expected, f"Expected {expected}, but got {result}")

    def test_data_integrity(self):  # data integrity test before encryption and after decryption
        path_to_image = 'tests/fixtures/test_encrypt_text.png'
        with open(path_to_image, 'rb') as file:
            text = file.read()
        password = 'qwerty123'
        encrypted_data = encrypt_text(text, password)
        decrypted_data = decrypt_text(encrypted_data, password)
        self.assertEqual(decrypted_data, text, f"Expected {text}, but got {decrypted_data}")


class TestDecryptText(unittest.TestCase):
    list_files = [
        'tests/fixtures/test_decrypt_text.jpg',
        'tests/fixtures/test_decrypt_text.pdf',
    ]

    def random_file(list_files):
        if not list_files:
            return None
        else:
            return random.choice(list_files)

    def random_password(length=20):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password

    def test_random_data(self):
        path_to_image = TestDecryptText.random_file(TestDecryptText.list_files)
        password = TestDecryptText.random_password()

        with open(path_to_image, 'rb') as file:
            text = file.read()
        encrypted_data = encrypt_text(text, password)
        decrypted_data = decrypt_text(encrypted_data, password)

        self.assertEqual(decrypted_data, text, f"Expected {text}, but got {decrypted_data}")


class TestCleanExit(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_clean_exit(self, mock_stdout):
        expected_message = "qwerty123"
        with self.assertRaises(SystemExit) as context:
            clean_exit(expected_message)
        self.assertEqual(context.exception.code, 0)
        self.assertEqual(mock_stdout.getvalue().strip(), expected_message)


if __name__ == "__main__":
    unittest.main()
