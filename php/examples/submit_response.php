<?

require_once('../EpiDBClient.php');
require('config.php');

$api_key = $_api_key;
$user_id = $_user_id;
$survey_id = $_survey_id;
$answers = array('q1' => 1,
                 'q2' => True,
                 'q3' => array( 1, 2, 3 ),
                 'q4' => 'Jakarta');

// If $date is null, the current date and time will be used
//   $date = null;
$date = '2009-12-15 01:02:03';

$client = new EpiDBClient($api_key);
$client->server = $_server; // Use this if you want to override
                            // the server location
$result = $client->response_submit($user_id, $survey_id, $answers, $date);

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

