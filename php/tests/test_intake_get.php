<?

require_once('../EpiDBClient.php');
require_once('config.php');

$key = $_key;

$client = new EpiDBClient($key);
$client->server = $_server;
$res = $client->intake_get($_user_id, '');

print "$res\n";

// vim: ts=4 sts=4 expandtab

