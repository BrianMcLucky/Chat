import sys
import unittest
from lesson3.common import utils

sys.path.append('../lesson3/')


class TestChat(unittest.TestCase):
    def setUp(self):
        self.s = utils.get_serv_socket('127.0.0.1', 7777)
        self.c = utils.get_user_socket('127.0.0.1', 7777)
        self.sender = self.s.accept()[0]

        utils.send_data(self.c, {'test': 'test'})

    def tearDown(self):
        self.c.close()
        self.s.close()

    def test_get_data(self):
        self.assertEqual(utils.get_data(self.sender), {'test': 'test'})

    def test_send_data(self):
        with self.assertRaises(TypeError):
            utils.send_data()


if __name__ == '__main__':
    unittest.main()
