import os
import sys
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
        pass

    def test_SaveSingleMsg(self):
        # normal condition
        self.assertTrue(storage.saveSingleMsg(sender=u"Alex", receiver=u"Tom", msg=u"Hello!"))
        # missing required args
        self.assertRaises(TypeError, storage.saveSingleMsg, )
        # getting unexpected args
        self.assertRaises(TypeError, storage.saveSingleMsg, unkown="Tom")
        self.assertRaises(TypeError, storage.saveSingleMsg, "unkown arg")
        # required args being empty
        self.assertFalse(storage.saveSingleMsg(sender="", receiver="", msg=""))

    def test_SaveGroupMsg(self):
        # normal condition
        self.assertTrue(storage.saveGroupMsg(sender=u"Alex", group_id=10001, msg=u"Hi, everyone!"))
        # missing required args
        self.assertRaises(TypeError, storage.saveGroupMsg, )
        # getting unexpected args
        self.assertRaises(TypeError, storage.saveGroupMsg, unkown="Tom")
        self.assertRaises(TypeError, storage.saveGroupMsg, "unkown arg")
        # required args being empty
        self.assertFalse(storage.saveGroupMsg(sender="", group_id="", msg=""))

    def test_SavePicture(self):
        # normal condition
        status_code, path = storage.savePicture(content="abcdefg",format=".jpg")
        self.assertEqual(status_code, True)
        import hashlib
        md5 = hashlib.md5()
        md5.update("abcdefg")
        pic_name = md5.hexdigest()
        self.assertEqual(path, pic_name+".jpg")
        # missing required args
        self.assertRaises(TypeError, storage.savePicture, )
        # getting unexpected args
        self.assertRaises(TypeError, storage.savePicture, sender="")
        # required args being empty
        self.assertFalse(storage.savePicture(content="",format=""))


if __name__ == '__main__':
    unittest.main()
