<?

if (!function_exists('json_encode') || !function_exists('json_decode')) {
    if (!class_exists('Services_JSON')) {
        require_once('Services_JSON.php');
    }
}

define('EPIDB_CLIENT_VERSION', '0.1.5');
define('EPIDB_CLIENT_AGENT', 
       'EpiDB-Client/' . EPIDB_CLIENT_VERSION . ' (php)');

class EpiDBClient {

    var $version = EPIDB_CLIENT_VERSION;
    var $__user_agent = EPIDB_CLIENT_AGENT;

    var $server = 'https://egg.science.uva.nl:7443';
    var $path_response = '/response/';
    var $path_profile = '/profile/';
    var $api_key = '';

    function __construct($api_key=null) {
        $this->api_key = $api_key;
    }

    function EpiDBClient($api_key=null) {
        $this->__construct($api_key);
    }

    function __epidb_encode($data) {
        $res = array();
        foreach ($data as $key=>$val) {
            $res[] = $key . '=' . urlencode($val);
        }
        return implode('&', $res);
    }

    function __epidb_call($url, $data=null) {
        $param = '';
        if ($data !== null) {
            $param = $this->__epidb_encode($data);
        }

        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        if ($data !== null) {
            curl_setopt($ch, CURLOPT_POST, count($data));
            curl_setopt($ch, CURLOPT_POSTFIELDS, $param);
        }
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 2);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_USERAGENT, $this->__user_agent);
        if ($this->api_key != null) {
            curl_setopt($ch, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
            $userpwd = $this->api_key . ':' . $this->api_key;
            curl_setopt($ch, CURLOPT_USERPWD, $userpwd);
        }
        $res = curl_exec($ch);
        curl_close($ch);

        return $res;
    }

    function __json_encode($data) {
        if (function_exists('json_encode')) {
            return json_encode($data);
        }
        else {
            $obj = new Services_JSON();
            return $obj->encode($data);
        }
    }

    function __json_decode($json) {
        if (function_exists('json_decode')) {
            return json_decode($json, true);
        }
        else {
            $obj = new Services_JSON(SERVICES_JSON_LOOSE_TYPE);
            return $obj->decode($json);
        }
    }

    function __wrap($data) {
        return $this->__json_encode($data);
    }

    function __unwrap($res) {
        return $this->__json_decode($res);
    }

    function response_submit($data) {
        $param = array();
        $param['data'] = $this->__wrap($data);
        $url = $this->server . $this->path_response;
        $res = $this->__epidb_call($url, $param);
        return $this->__unwrap($res);
    }

    function profile_update($user_id, $data) {
        $param = array();
        $param['data'] = $this->__wrap($data);
        $url = $this->server . $this->path_profile . $user_id . '/';
        $res = $this->__epidb_call($url, $param);
        return $this->__unwrap($res);
    }

    function profile_get($user_id) {
        $url = $this->server . $this->path_profile . $user_id . '/';
        $res = $this->__epidb_call($url);
        return $this->__unwrap($res);
    }

};

// vim: ts=4 sts=4 expandtab

