<?

require_once('../EpiDBClient.php');
require_once('config.php');

$key = $_key;
$data = array(
    'name' => 'John Doe',
    'address' => 'Jakarta'
);

$client = new EpiDBClient();
$client->server = $_server;
$res = $client->profile_update($_user_id, $data);

var_dump($res);

// vim: ts=4 sts=4 expandtab

