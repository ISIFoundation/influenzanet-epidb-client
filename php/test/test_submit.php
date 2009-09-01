<?

require_once('../EpiDBClient.php');

$client = new EpiDBClient();
$client->submit('{ "source": "php" }');

