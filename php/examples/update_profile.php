<?

require_once('../EpiDBClient.php');
require('config.php');

$api_key = $_api_key;
$user_id = $_user_id;
$profile_survey_id = $_profile_survey_id;
$answers = array('birth-place' => 'Jakarta',
                 'birth-day' => '2009-09-09',
                 'has-pets' => False);

// If $date is null, the current date and time will be used
//   $date = null;
$date = '2009-12-15 01:02:03';

$client = new EpiDBClient($api_key);
$client->server = $_server; // Use this if you want to override
                            // the server location
$result = $client->profile_update($user_id, $survey_id, $answers, $date);

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

