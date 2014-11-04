# -*- coding:utf-8 -*-
import os
import sys
import time
import unittest
import httplib
import json

def initPath():
    project_path = os.path.dirname(
        os.path.dirname(os.path.dirname(__file__)))
    sys.path.insert(0, project_path)

initPath()

class testClients(unittest.TestCase):
    """docstring for testClients
       bugs: process will not automatically exit after execution,
             has to be terminated manually, reason to be found.
    """
    def setUp(self):
        self._server_ip = "127.0.0.1"
        self._server_port = 5000
        self.connection = httplib.HTTPConnection(self._server_ip,self._server_port)
        self._message_pool = ["你好啊,今天天气不错","是的啊,有什么打算出游么",
                                "没有啊，你呢？","我不知道呢，还在家里看电视"]
        self._sender_pool = ["Alex", "Tom"]

    def test_SaveSingleMsg(self):
        for i in xrange(100):
            headers = {"Content-type":"application/json; charset=UTF-8"}
            data = {"sender":self._sender_pool[i%len(self._sender_pool)],
                    "receiver":self._sender_pool[(i+1)%len(self._sender_pool)],
                    "message":[time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),
                                self._message_pool[i%len(self._message_pool)]]}
            self.connection.request("POST", "/saveSingleMsg/",
                json.JSONEncoder().encode(data), headers)
            response = self.connection.getresponse()
            self.assertEqual(response.read(), "Singe message saved.")

    def test_SaveGroupMsg(self):
        for i in xrange(100):
            headers = {"Content-type":"application/json; charset=UTF-8"}
            data = {"sender":self._sender_pool[i%len(self._sender_pool)],
                    "group_id":"10011",
                    "message":[time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),
                                self._message_pool[i%len(self._message_pool)]]}
            self.connection.request("POST", "/saveGroupMsg/",
                json.JSONEncoder().encode(data), headers)
            response = self.connection.getresponse()
            self.assertEqual(response.read(), "Group message saved.")

    def test_SavePicture(self):
        headers = {"Content-type":"application/json; charset=UTF-8"}
        data = {"content":os.urandom(4096).encode("hex"), "format":".jpg"}
        self.connection.request("POST", "/savePicture/",
            json.JSONEncoder().encode(data), headers)
        response = self.connection.getresponse()
        self.assertEqual(response.read(), "Picture saved.")

    def tearDown(self):
        self.connection.close()

if __name__ == '__main__':
    unittest.main()
