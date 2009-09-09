<?

require_once('../EpiDBClient.php');
require_once('config.php');

$key = $_key;
$data = 'data';

$client = new EpiDBClient();
$client->server = $_server;
$res = $client->update_profile($_user_id, $data);

print "$res\n";

// vim: ts=4 sts=4 expandtab

