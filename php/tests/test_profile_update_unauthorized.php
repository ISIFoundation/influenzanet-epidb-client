<?

require_once('../EpiDBClient.php');
require_once('config.php');

$key = $_key;
$data = 'data';

$client = new EpiDBClient();
$client->server = $_server;
$res = $client->profile_update($_user_id, $data);

print "$res\n";

// vim: ts=4 sts=4 expandtab

