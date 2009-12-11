import unittest

import epidb_client
from epidb_client import BasicClient, config

class LiveResponseSubmitTestCase(unittest.TestCase):
    def setUp(self):
        self.client = EpiDBClient(config.api_key)
        self.client.server = config.server

        self.data = {'user_id': config.user_id,
                     'date': '2009-09-09 09:09:09',
                     'answers': {'q0000': '0',
                                 'q0001': '1',
                                 'q0002': '2'}}

    def testSuccess(self):
        result = self.client.response_submit(self.data)
        self.assertEqual(result['stat'], 'ok')

class LiveResponseSubmitUnauthorizedTestCase(unittest.TestCase):
    def setUp(self):
        self.client = EpiDBClient(config.api_key_invalid)
        self.client.server = config.server

        self.data = {'user_id': config.user_id,
                     'date': '2009-09-09 09:09:09',
                     'answers': {'q0000': '0',
                                 'q0001': '1',
                                 'q0002': '2'}}

    def testUnauthorized(self):
        try:
            self.client.response_submit(self.data)
            self.fail()
        except epidb_client.ResponseError, e:
            self.assertEqual(e.code, 401)

if __name__ == '__main__':
    unittest.main()

# vim: set ts=4 sts=4 expandtab:

