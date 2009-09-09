<?

require_once('../EpiDBClient.php');
require_once('config.php');

$key = null;
$data = 'data';

$client = new EpiDBClient($key);
$client->server = $_server;
$res = $client->submit_response($data);

print "$res\n";

// vim: ts=4 sts=4 expandtab

