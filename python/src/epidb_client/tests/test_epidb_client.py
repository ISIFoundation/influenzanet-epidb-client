import unittest
import urllib

try:
    import simplejson as json
except ImportError:
    import json

import epidb_client
from epidb_client import BasicClient, config

from mocks import *

class EpiDbClientTestCase(unittest.TestCase):
    def setUp(self):
        self.urllib2 = MockUrllib2()
        self.urllib2_orig = epidb_client.urllib2
        epidb_client.urllib2 = self.urllib2

        self.client = EpiDBClient(config.api_key)
        self.client.server = config.server

    def tearDown(self):
        epidb_client.urllib2 = self.urllib2_orig 

    def testApiKey(self):
        self.assertEqual(self.client.api_key, config.api_key)

    def testResponseSubmitCall(self):
        eresult = '{"stat": "ok", "msg": "hello world!"}'
        dresult = json.loads(eresult)
        self.urllib2._result = eresult

        data = {'name': 'john doe+',
                'address': 'amsterdam'}

        res = self.client.response_submit(data)

        # Make sure the result is the same
        self.assertEqual(res, dresult)

        # Check sent data
        keys = map(lambda x: x.split('=')[0], self.urllib2.data.split('&'))
        self.assertEqual(sorted(keys), sorted(['data']))

        value = self.urllib2.data.split('=')[1]
        value = value.replace('+', ' ')
        value = urllib.unquote(value)
        dvalue = json.loads(value)
        self.assertEqual(data, dvalue)

        # Check API Key
        self.assertTrue('Cookie' in self.urllib2.request.headers)
        cookiestring = self.urllib2.request.headers['Cookie']
        cookie = filter(lambda x: x.startswith('epidb-apikey='), 
                        self.urllib2.request.headers['Cookie'].split('&'))
        k, v = cookie[0].split('=')
        self.assertEqual(k, 'epidb-apikey')
        self.assertEqual(v, config.api_key)

        # Check URL
        self.assertEqual("%sresponse/" % config.server, self.urllib2.request.url)

    def testProfuleUpdateCall(self):
        eresult = '{"stat": "ok", "msg": "hello world!"}'
        dresult = json.loads(eresult)
        self.urllib2._result = eresult

        data = {'name': 'john doe+',
                'address': 'amsterdam'}

        res = self.client.profile_update(config.user_id, data)

        # Make sure the result is the same
        self.assertEqual(res, dresult)

        # Check sent data
        keys = map(lambda x: x.split('=')[0], self.urllib2.data.split('&'))
        self.assertEqual(sorted(keys), sorted(['data']))

        value = self.urllib2.data.split('=')[1]
        value = value.replace('+', ' ')
        value = urllib.unquote(value)
        dvalue = json.loads(value)
        self.assertEqual(data, dvalue)

        # Check API Key
        self.assertTrue('Cookie' in self.urllib2.request.headers)
        cookiestring = self.urllib2.request.headers['Cookie']
        cookie = filter(lambda x: x.startswith('epidb-apikey='), 
                        self.urllib2.request.headers['Cookie'].split('&'))
        k, v = cookie[0].split('=')
        self.assertEqual(k, 'epidb-apikey')
        self.assertEqual(v, config.api_key)

        # Check URL
        self.assertEqual("%sprofile/%s/" % (config.server, config.user_id), 
                         self.urllib2.request.url)

    def testURL(self):
        eresult = '{"stat": "ok"}'
        self.urllib2._result = eresult

        baseurl = "http://epiwork.eu"
        expected = "%s/response/" % baseurl

        self._test_url(expected, "http://epiwork.eu")
        self._test_url(expected, "http://epiwork.eu/")
        self._test_url(expected, "http://epiwork.eu//")
        self._test_url(expected, "http://epiwork.eu ")
        self._test_url(expected, "http://epiwork.eu  ")
        self._test_url(expected, "http://epiwork.eu /")
        self._test_url(expected, "http://epiwork.eu  /")
        self._test_url(expected, "http://epiwork.eu //")
        self._test_url(expected, " http://epiwork.eu //")

    def _test_url(self, expected, url):
        data = {}
        self.client.server = url
        res = self.client.response_submit(data)
        self.assertEqual(expected, self.urllib2.request.url)

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


if __name__ == '__main__':
    unittest.main()

