<?

class EpiDBClient {

    var $version = '0.0~20090906.1';
    var $__user_agent = 'EpiDB-Client/0.0~20090906.1 (php)';

    var $server = 'https://egg.science.uva.nl:7443';
    var $path_survey = '/survey/';
    var $path_intake = '/intake/';
    var $api_key = '';

    function __construct($api_key=null) {
        $this->api_key = $api_key;
    }

    function EpiDBClient($api_key='') {
        $this->__construct($api_key);
    }

    function __epidb_encode($data) {
        $res = array();
        foreach ($data as $key=>$val) {
            $res[] = $key . '=' . urlencode($val);
        }
        return implode('&', $res);
    }

    function __epidb_call($url, $data) {
        $param = $this->__epidb_encode($data);

        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_POST, count($data));
        curl_setopt($ch, CURLOPT_POSTFIELDS, $param);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 2);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_USERAGENT, $this->__user_agent);
        curl_setopt($ch, CURLOPT_COOKIE, "epidb-apikey=" . $this->api_key);
        $res = curl_exec($ch);
        curl_close($ch);

        return $res;
    }

    function survey_submit($data) {
        $param = array();
        $param['data'] = $data;
        $url = $this->server . $this->path_survey;
        $res = $this->__epidb_call($url, $param);
        return $res;
    }

    function intake_submit($user_id, $data) {
        $param = array();
        $param['data'] = $data;
        $url = $this->server . $this->path_intake . $user_id . '/';
        $res = $this->__epidb_call($url, $param);
        return $res;
    }

};

// vim: ts=4 sts=4 expandtab

