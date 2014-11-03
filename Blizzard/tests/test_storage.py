# -*- coding: utf-8 -*-
import os
import sys
import time
import unittest

def initPath():
    project_path = os.path.dirname(
        os.path.dirname(os.path.dirname(__file__)))
    sys.path.insert(0, project_path)

initPath()

from Blizzard import storage

class testStorage(unittest.TestCase):
    """docstring for testStorage"""
    def setUp(self):
        self.saver = storage.MessageSaver(test_mode=True)

    def test_SaveSingleMsg(self):
        # normal condition
        self.assertTrue(self.saver.saveSingleMsg(sender="Alex",
            receiver="Tom", msg=[time.strftime(
                "%Y-%m-%d %H:%M:%S",time.localtime()), "你好!天气不错"]))
        # missing required args
        self.assertRaises(TypeError, self.saver.saveSingleMsg, )
        # getting unexpected args
        self.assertRaises(TypeError, self.saver.saveSingleMsg, unkown="Tom")
        self.assertRaises(TypeError, self.saver.saveSingleMsg, "unkown arg")
        # required args being empty
        self.assertFalse(self.saver.saveSingleMsg(
            sender="", receiver="", msg=[]))

    def test_SaveGroupMsg(self):
        # normal condition
        self.assertTrue(self.saver.saveGroupMsg(sender="Alex",
            group_id="10001", msg=[time.strftime(
                "%Y-%m-%d %H:%M:%S",time.localtime()), "Hi, everyone!"]))
        # missing required args
        self.assertRaises(TypeError, self.saver.saveGroupMsg, )
        # getting unexpected args
        self.assertRaises(TypeError, self.saver.saveGroupMsg, unkown="Tom")
        self.assertRaises(TypeError, self.saver.saveGroupMsg, "unkown arg")
        # required args being empty
        self.assertFalse(self.saver.saveGroupMsg(
            sender="", group_id="", msg=[]))

    def test_SavePicture(self):
        # normal condition
        path = self.saver.savePicture(content="abcdefg",format_=".jpg")
        import hashlib
        md5 = hashlib.md5()
        md5.update("abcdefg")
        pic_name = md5.hexdigest()
        self.assertEqual(path, pic_name+".jpg")
        # missing required args
        self.assertRaises(TypeError, self.saver.savePicture, )
        # getting unexpected args
        self.assertRaises(TypeError, self.saver.savePicture, sender="")
        # required args being empty
        self.assertFalse(self.saver.savePicture(content="",format_=""))

    def tearDown(self):
        time.sleep(3)
        self.saver._MessageSaver__stop_writing()

if __name__ == '__main__':
    unittest.main()
