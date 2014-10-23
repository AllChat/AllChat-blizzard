# -*- coding: utf-8 -*-
class Encryptor(object):
    def __init__(self, key):
        self.key = key

    def EncryptStr(self,string):
        if not isinstance(string,unicode):
            raise TypeError
        hex_str = "".join([x.encode("hex").zfill(6) for x in string])
        encrypted_str = "".join([hex(int(hex_str[index*16:(index+1)*16],16)^self.key)[2:-1]
                                 for index in xrange(len(hex_str)/16+1)
                                 if hex_str[index*16:(index+1)*16]])
        return encrypted_str

    def DecryptStr(self,string):
        decrypted_str = ''
        
        return decryptedStr