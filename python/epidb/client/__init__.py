
import urllib
import urllib2

__version__ = '0.0~20090906.1'
__user_agent__ = 'EpiDB-Client/%s (python)' % __version__

class EpiDBClient:

    version = __version__
    user_agent = __user_agent__

    server = 'https://egg.science.uva.nl:7443'
    path_survey = '/survey/'
    path_intake = '/intake/'

    def __init__(self, api_key=None):
        self.api_key = api_key

    def __epidb_call(self, url, param=None):
        res = None
        sock = None

        try:
            if param is not None:
                data = urllib.urlencode(param)
            else:
                data = None

            req = urllib2.Request(url)
            req.add_header('User-Agent', self.user_agent)
            if self.api_key:
                req.add_header('Cookie', 'epidb-apikey=%s' % self.api_key)
            sock = urllib2.urlopen(req, data)
            res = sock.read()
            sock.close()
        except urllib2.HTTPError, e:
            res = e.read()

        return res
    
    def survey_submit(self, data):
        param = {
            'data': data
        }

        url = self.server + self.path_survey
        res = self.__epidb_call(url, param)

        return res

    def intake_submit(self, user_id, data):
        param = {
            'data': data
        }

        url = self.server + self.path_intake + user_id + '/'
        res = self.__epidb_call(url, param)

        return res

# vim: ts=4 sts=4 expandtab

