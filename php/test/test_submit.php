<?

include('../EpiDBClient.php');

$client = new EpiDBClient();
$client->submit('{ "source": "php" }', 'php');

