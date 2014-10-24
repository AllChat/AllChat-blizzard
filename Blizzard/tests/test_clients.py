import os
import sys
import unittest
import httplib

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
		connection.request("POST", "/saveSingleMsg")
		response = connection.getresponse()
		self.assertEqual(response.read(), "singe message saved.")

	def test_SaveGroupMsg(self):
		connection = httplib.HTTPConnection(self._server_ip,self._server_port)
		connection.request("POST", "/saveGroupMsg")
		response = connection.getresponse()
		self.assertEqual(response.read(), "group message saved.")

	def test_SavePicture(self):
		connection = httplib.HTTPConnection(self._server_ip,self._server_port)
		connection.request("POST", "/savePicture")
		response = connection.getresponse()
		self.assertEqual(response.read(), "picture saved.")

if __name__ == '__main__':
	unittest.main()
