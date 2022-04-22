import sys
import unittest
from lesson3.common import utils
import socket

sys.path.append('../lesson3/')


class TestServer(unittest.TestCase):
    def setUp(self):
        self.s = utils.get_serv_socket('127.0.0.1', 7777)

    def tearDown(self):
        self.s.close()

    def test_server_socket_is_socket(self):
        self.assertIsInstance(self.s, socket.socket)

    def test_server_socket_addr(self):
        self.assertEqual(self.s.getsockname(), ('127.0.0.1', 7777))


if __name__ == '__main__':
    unittest.main()
