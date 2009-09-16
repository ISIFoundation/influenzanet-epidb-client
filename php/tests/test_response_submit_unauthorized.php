<?

require_once('../EpiDBClient.php');
require_once('config.php');

$key = null;
$data = Array(
    'user_id' => $_user_id,
    'date' => '2009-09-09 09:09:09'
);

$client = new EpiDBClient($key);
$client->server = $_server;
$res = $client->response_submit($data);

var_dump($res);

// vim: ts=4 sts=4 expandtab

