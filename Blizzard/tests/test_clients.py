import os
import sys
import unittest

def initPath():
    project_path = os.path.dirname(
        os.path.dirname(os.path.dirname(__file__)))
    sys.path.insert(0, project_path)

initPath()

from Blizzard import clients

class testClients(unittest.TestCase):
	"""docstring for testClients"""
	def setUp(self):
		pass

	def test_SaveMsg(self):
		pass

if __name__ == '__main__':
	unittest.main()
