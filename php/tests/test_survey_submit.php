<?

require_once('../EpiDBClient.php');
require_once('config.php');

$key = $_key;
$data = 'data';

$client = new EpiDBClient($key);
$client->server = $_server;
$res = $client->survey_submit($data);

print "$res\n";

// vim: ts=4 sts=4 expandtab

