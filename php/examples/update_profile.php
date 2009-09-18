<?

// This example requires JSON library that is available
// in PHP 5.2 or later or json PECL package.

require_once('../EpiDBClient.php');

$api_key = 'your-epidb-api-key-here';
$user_id = '1c66bb91-33fd-4c6c-9c11-8ddd94164ae8';
$data = array(
    'birth-place' => 'Jakarta',
    'birth-day' => '2009-09-09',
    'has-pets' => False
);

$client = new EpiDBClient($api_key);
$result = $client->profile_update($user_id, $data);

$status = $result['stat'];

header('Content-Type: text/plain');

print("status: " . $status . "\n");

if ($status != 'ok') {
    print("error code: " . $result['code'] . "\n");
    print("       msg: " . $result['msg'] . "\n");
}

