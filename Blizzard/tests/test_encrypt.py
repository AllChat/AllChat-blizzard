# -*- coding: utf-8 -*-
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
        key = os.urandom(16).encode("hex")
        self.encryptor = encrypt.Encryptor(int(key, 16))
        
    def test_Encryptor(self):
        original_str = "0123;abcd,你说的对!@$#%"
        encrypted_str = self.encryptor.EncryptStr(original_str)
        self.assertNotEqual(original_str, encrypted_str)
        decrypted_str = self.encryptor.DecryptStr(encrypted_str)
        self.assertEqual(original_str, decrypted_str)
        
if __name__=="__main__":
    unittest.main()