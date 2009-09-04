<?

require_once('../EpiDBClient.php');

$data = 'data';

$client = new EpiDBClient();
$res = $client->survey_submit($data);

print "$res\n";

