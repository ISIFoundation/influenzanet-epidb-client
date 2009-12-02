import unittest
import urllib
import urllib2

try:
    import simplejson as json
except ImportError:
    import json

import epidb_client
from epidb_client import BasicClient

import config
from mocks import *

class BasicClientTestCase(unittest.TestCase):
    def setUp(self):
        self.urllib2 = MockUrllib2()
        self.urllib2_orig = epidb_client.urllib2
        epidb_client.urllib2 = self.urllib2

        self.client = BasicClient()

    def tearDown(self):
        epidb_client.urllib2 = self.urllib2_orig 

    def testParam(self):
        self.urllib2._result = None

        self.client._send(config.server)

        # Verify the URL
        self.assertEqual(config.server, self.urllib2.request.url)

        # GET request with no data means the data is None
        self.assertEqual(None, self.urllib2.data)

    def testPostEmpty(self):
        self.urllib2._result = None

        # POST request with no data means create request with an empty data
        self.client._send(config.server, method='POST')
        self.assertEqual('', self.urllib2.data)

    def testVerifyData(self):
        self.urllib2._result = None

        # Verify the data we send
        param = {'data': 'the data',
                 'number': 'is a text'}
        self.client._send(config.server, param=param)
        self._testEncodedData(param, self.urllib2.data)

    def testUserAgentCookie(self):
        self.urllib2._result = None

        # Make sure User-Agent string is added
        self.client._send(config.server)
        self.assertTrue('User-Agent' in self.urllib2.request.headers.keys())

        # Cookie header does not exist if no Cookie is set
        self.assertFalse('Cookie' in self.urllib2.request.headers.keys())

    def testCookie(self):
        self.urllib2._result = None

        # Cookie is a header with key 'Cookie'
        cookies = {'epidb-apikey': '1234567890',
                   'session_id': 'abcdef'}
        self.client._send(config.server, cookies=cookies)
        self.assertTrue('User-Agent' in self.urllib2.request.headers.keys())
        self.assertTrue('Cookie' in self.urllib2.request.headers.keys())
        self._testEncodedData(cookies, self.urllib2.request.headers['Cookie'])

    def _testEncodedData(self, data, encoded):
        keys = []
        for item in encoded.split('&'):
            k, v = item.split('=')
            keys.append(k)
            self.assertTrue(k in data.keys())
            
            # Check the encoded value, one by one
            e = urllib.urlencode({k: data[k]})
            self.assertEqual(e, item)
        self.assertEqual(sorted(keys), sorted(data.keys()))

    def testValidResult(self):
        eresult = '{"stat": "ok", "msg": "hello world!"}'
        dresult = json.loads(eresult)

        self.urllib2._result = eresult

        res = self.client._call(config.server)
        self.assertEqual(res, dresult)

    def testInvalidResponse(self):
        eresult = 'not a json document'

        self.urllib2._result = eresult

        self.assertRaises(epidb_client.InvalidResponseError, 
                          self.client._call, config.server)

    def testErrorResponse(self):
        code = "123456"
        msg = "error message"

        eresult = '{"stat": "fail", "code": "%s", "msg": "%s"}' % (code, msg)
        dresult = json.loads(eresult)

        self.urllib2._error = eresult
        try:
            self.client._call(config.server)
            self.fail()
        except epidb_client.ResponseError, e:
            self.assertEqual(e.code, code)
            self.assertEqual(e.msg, msg)

    def testOtherError(self):
        code = "123456"
        msg = "error message"

        eresult = '{"stat": "fail", "code": "%s", "msg": "%s"}' % (code, msg)
        dresult = json.loads(eresult)

        self.urllib2._error = RuntimeError()
        self.assertRaises(RuntimeError, self.client._call, config.server)

    def testUnknownOtherError(self):
        eresult = 'not a json document'
        self.urllib2._error = eresult

        self.urllib2._error = RuntimeError()
        self.assertRaises(RuntimeError, self.client._call, config.server)

    def testUnknownHttpError(self):
        eresult = 'not a json document'
        self.urllib2._error = eresult

        try:
            self.client._call(config.server)
            self.fail()
        except self.urllib2.HTTPError, e:
            self.assertEqual(e.read(), eresult)

    def testInvalidStatus(self):
        # What if a 200 OK response returns an error message?
        code = "123456"
        msg = "error message"

        eresult = '{"stat": "fail", "code": "%s", "msg": "%s"}' % (code, msg)
        dresult = json.loads(eresult)

        self.urllib2._result = eresult
        self.assertRaises(epidb_client.InvalidResponseError, self.client._call,
                          config.server)

    def testInvalidMessageNoStat(self):
        eresult = '{"msg": "hello world!"}'
        dresult = json.loads(eresult)

        self.urllib2._result = eresult
        self.assertRaises(epidb_client.InvalidResponseError, self.client._call,
                          config.server)

    def testInvalidMessageNoStatError(self):
        eresult = '{"msg": "hello world!"}'
        dresult = json.loads(eresult)

        self.urllib2._error = eresult
        self.assertRaises(epidb_client.InvalidResponseError, self.client._call,
                          config.server)

    def testInvalidMessageNoCode(self):
        eresult = '{"stat": "fail", "msg": "hello world!"}'

        self.urllib2._error = eresult
        self.assertRaises(epidb_client.InvalidResponseError, self.client._call,
                          config.server)

    def testInvalidMessageNoMsg(self):
        eresult = '{"stat": "fail", "code": "123"}'

        self.urllib2._error = eresult
        self.assertRaises(epidb_client.InvalidResponseError, self.client._call,
                          config.server)

    def testInvalidMessageNoCodeMsg(self):
        eresult = '{"stat": "fail"}'

        self.urllib2._error = eresult
        self.assertRaises(epidb_client.InvalidResponseError, self.client._call,
                          config.server)

    def testInvalidMessage(self):
        eresult = '{"hello": "world"}'

        self.urllib2._result = eresult
        self.assertRaises(epidb_client.InvalidResponseError, self.client._call,
                          config.server)

    def testInvalidMessageError(self):
        eresult = '{"hello": "world"}'

        self.urllib2._error = eresult
        self.assertRaises(epidb_client.InvalidResponseError, self.client._call,
                          config.server)

    def testApiKey(self):
        self.urllib2._result = '{"stat": "ok"}'

        # Make sure User-Agent string is added
        self.client._auth_call(config.server, config.api_key)
        self.assertTrue('User-Agent' in self.urllib2.request.headers.keys())

        # API Key is sent as cookie
        self.assertTrue('Cookie' in self.urllib2.request.headers.keys())
        cookie = filter(lambda x: x.startswith('epidb-apikey='), 
                        self.urllib2.request.headers['Cookie'].split('&'))
        k, v = cookie[0].split('=')
        self.assertEqual(k, 'epidb-apikey')
        self.assertEqual(v, config.api_key)

    def testSessionId(self):
        self.urllib2._result = '{"stat": "ok"}'

        # Make sure User-Agent string is added
        self.client._admin_call(config.server, config.session_id)
        self.assertTrue('User-Agent' in self.urllib2.request.headers.keys())

        # Session ID is sent as cookie
        self.assertTrue('Cookie' in self.urllib2.request.headers.keys())
        cookie = filter(lambda x: x.startswith('session_id='), 
                        self.urllib2.request.headers['Cookie'].split('&'))
        k, v = cookie[0].split('=')
        self.assertEqual(k, 'session_id')
        self.assertEqual(v, config.session_id)

if __name__ == '__main__':
    unittest.main()

