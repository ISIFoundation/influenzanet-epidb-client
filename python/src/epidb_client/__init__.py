import urllib
import urllib2

try:
    import simplejson as json
except ImportError:
    import json

__version__ = '0.1.1'
__user_agent__ = 'EpiDB-Client/%s (python)' % __version__

class InvalidResponseError(Exception):
    pass

class ResponseError(Exception):
    def __init__(self, code, msg, *args, **kwargs):
        self.code = code
        self.msg = msg
        Exception.__init__(self, *args, **kwargs)

class BasicClient:
    version = __version__
    user_agent = __user_agent__

    def _send(self, url, method='GET', param={}, cookies={}):
        data = None
        if param:
            data = urllib.urlencode(param)

        if method == 'POST' and data is None:
            data = ''

        req = urllib2.Request(url)
        req.add_header('User-Agent', self.user_agent)
        
        if cookies:
            req.add_header('Cookie', urllib.urlencode(cookies))

        sock = urllib2.urlopen(req, data)
        res = sock.read()
        sock.close()

        return res

    def _call(self, url, method='GET', param={}, cookies={}):
        res = None
        err = None

        try:
            res = self._send(url, method, param, cookies)
        except urllib2.HTTPError, e:
            err = e
            res = e.read()

        try:
            data = json.loads(res)
            if err is not None:
                if data.get('stat', None) != 'fail' or \
                        data.get('code', None) is None or \
                        data.get('msg', None) is None:
                    raise InvalidResponseError()
                raise ResponseError(data['code'], data['msg'])
            if data.get('stat', None) != 'ok':
                raise InvalidResponseError()
            return data
        except ValueError:
            if err is not None:
                raise err
            raise InvalidResponseError()

    def _auth_call(self, url, api_key, method='GET', param={}, cookies={}):
        cookies['epidb-apikey'] = api_key
        return self._call(url, method, param, cookies)

    def _admin_call(self, url, session_id, method='GET', param={}, cookies={}):
        cookies['session_id'] = session_id
        return self._call(url, method, param, cookies)

class EpiDBClient(BasicClient):

    server = 'https://egg.science.uva.nl:7443'
    path_response = '/response/'
    path_profile = '/profile/'

    def __init__(self, api_key=None):
        self.api_key = api_key

    def _get_server(self):
        return self.server.strip().rstrip(' /')

    def response_submit(self, data):
        param = {
            'data': json.dumps(data)
        }

        url = self._get_server() + self.path_response
        res = self._auth_call(url, self.api_key, method='POST', param=param)

        return res

    def profile_update(self, user_id, data):
        param = {
            'data': json.dumps(data)
        }

        url = self._get_server() + self.path_profile + user_id + '/'
        res = self._auth_call(url, self.api_key, method='POST', param=param)

        return res

# vim: set ts=4 sts=4 expandtab:

