<?

require_once('../EpiDBClient.php');

$key = '0123456789abcdef0123456789abcdef01234567';
$data = 'data';

$client = new EpiDBClient($key);
$res = $client->survey_submit($data);

print "$res\n";

