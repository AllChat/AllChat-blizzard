import os
import sys
import unittest
import random

def initPath():
    project_path = os.path.dirname(
        os.path.dirname(os.path.dirname(__file__)))
    sys.path.insert(0, project_path)

initPath()

from Blizzard import encrypt

class testEncrypt(unittest.TestCase):
    def setUp(self):
        self.encryptor = encrypt.Encryptor(random.randint(1000000, 100000000))
        
    def test_Encryptor(self):
        original_str = u"Äã¹þ£¬°¢ÖÒ123"
        encrypted_str = self.encryptor.EncryptStr(original_str)
        self.assertNotEqual(original_str, encrypted_str)
        decrypted_str = self.encryptor.DecryptStr(encrypted_str)
        self.assertEqual(original_str, decrypted_str)
        
if __name__=="__main__":
    unittest.main()