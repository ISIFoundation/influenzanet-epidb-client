
import urllib

__version__ = '0.0~20090901.1'

class EpiDBClient:

	version = __version__

	server = 'https://egg.science.uva.nl:7443'
	path_submit = '/submit/'

	def __init__(self, api_key=''):
		self.api_key = api_key

	def __epidb_call(self, url, param):
		data = urllib.urlencode(param)
		sock = urllib.urlopen(url, data)
		res = sock.read()
		sock.close()

		return res
	
	def submit(self, data):
		param = {
			'data': data,
			'source': '',
			'format': ''
		}

		url = self.server + self.path_submit
		res = self.__epidb_call(url, param)

