<?

require_once('../EpiDBClient.php');

$data = 'data';

$client = new EpiDBClient();
$client->submit($data);

