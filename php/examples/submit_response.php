<?

// This example requires JSON library that is available
// in PHP 5.2 or later or json PECL package.

require_once('../EpiDBClient.php');

$api_key = 'your-epidb-api-key-here';
$data = array(
    'user_id' => '1c66bb91-33fd-4c6c-9c11-8ddd94164ae8',
    'date' => '2009-09-09 09:09:09',
    'answers' => array(
        'q1' => 1,
        'q2' => True,
        'q3' => array( 1, 2, 3 ),
        'q4' => 'Jakarta'
    )
);

$client = new EpiDBClient($api_key);
$result = $client->response_submit($data);

$status = $result['stat'];

header('Content-Type: text/plain');

print("status: " . $status . "\n");

if ($status == 'ok') {
    print("id: " . $result['id'] . "\n");
}
else {
    print("error code: " . $result['code'] . "\n");
    print("       msg: " . $result['msg'] . "\n");
}

