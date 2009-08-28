<?

class EpiDBClient {

	private $server = 'https://egg.science.uva.nl:7443';
	private $path_submit = '/submit/';

	public function __construct() {
	}

	private function __epidb_encode($data) {
		$res = array();
		foreach ($data as $key=>$val) {
			$res[] = $key . '=' . urlencode($val);
		}
		return implode('&', $res);
	}

	private function __epidb_call($url, $data) {
		$param = $this->__epidb_encode($data);

		$ch = curl_init();
		curl_setopt($ch, CURLOPT_URL, $url);
		curl_setopt($ch, CURLOPT_POST, count($data));
		curl_setopt($ch, CURLOPT_POSTFIELDS, $param);
		curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
		curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 2);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
		$res = curl_exec($ch);
		curl_close($ch);

		return $res;
	}

	public function submit($data, $source, $format='json') {
		$param = array();
		$param['data'] = $data;
		$param['source'] = $source;
		$param['format'] = $format;
		$url = $this->server . $this->path_submit;
		$res = $this->__epidb_call($url, $param);
	}



};

