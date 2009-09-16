<?

require_once('../EpiDBClient.php');
require_once('config.php');

$key = $_key;

$client = new EpiDBClient($key);
$client->server = $_server;
$res = $client->profile_get($_user_id, '');

var_dump($res);

// vim: ts=4 sts=4 expandtab

