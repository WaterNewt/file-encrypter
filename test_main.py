import unittest
from utils import *

class TestCLI(unittest.TestCase):
    def test_decrypt(self):
        self.assertEqual(decrypt_text(b'gAAAAABllTEUfhs83IeO4gOmeOUjLBWAr2kHDxE4WXEOKTuKQ-iEEEo7lVIKCa0-aZk0l895bRGc8nE8DMMXuOPFXLoc2isZDA==', "test"), b"Hello")
    
    def test_encrypt(self):
        self.assertEqual(decrypt_text(encrypt_text(b"Hello", "test"), "test"), b'Hello')
        
if __name__ == "__main__":
    unittest.main()