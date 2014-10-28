# -*- coding:utf-8 -*-
import os
import sys
import unittest
import httplib
import json

def initPath():
    project_path = os.path.dirname(
        os.path.dirname(os.path.dirname(__file__)))
    sys.path.insert(0, project_path)

initPath()

from Blizzard import clients

class testClients(unittest.TestCase):
    """docstring for testClients"""
    def setUp(self):
        self._server_ip = "127.0.0.1"
        self._server_port = 5000

    def test_SaveSingleMsg(self):
        connection = httplib.HTTPConnection(self._server_ip,self._server_port)
        headers = {"Content-type":"application/json; charset=UTF-8"}
        data = {"sender":"Alex", "receiver":"Tom", 
                "msg":"你好啊,今天天气不错"}
        connection.request("POST", "/saveSingleMsg",
            json.JSONEncoder().encode(data), headers)
        response = connection.getresponse()
        self.assertEqual(response.read(), "singe message saved.")

    def test_SaveGroupMsg(self):
        connection = httplib.HTTPConnection(self._server_ip,self._server_port)
        headers = {"Content-type":"application/json; charset=UTF-8"}
        data = {"sender":"Alex", "group_id":"10011", 
                "msg":"你好啊,今天天气不错"}
        connection.request("POST", "/saveGroupMsg")
        response = connection.getresponse()
        self.assertEqual(response.read(), "group message saved.")

    def test_SavePicture(self):
        connection = httplib.HTTPConnection(self._server_ip,self._server_port)
        headers = {"Content-type":"application/json; charset=UTF-8"}
        data = {"content":"dsamfeoingsafkg", "format":".jpg"}
        connection.request("POST", "/savePicture")
        response = connection.getresponse()
        self.assertEqual(response.read(), "picture saved.")

if __name__ == '__main__':
    unittest.main()
