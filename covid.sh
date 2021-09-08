DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATHS=$(echo $DATA | jq '.[0].death')
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalized')
TOTALTESTRESULTS=$(echo $DATA | jq '.[0].totalTestResults')
DEATHINCREASE=$(echo $DATA | jq '.[0].deathIncrease')
PENDING=$(echo $DATA | jq '.[0].pending')

echo "On $TODAY, there were $POSITIVE positive COVID cases, $NEGATIVE negative tests, $PENDING pending tests,  $DEATHS deaths, with a $DEATHINCREASE death increase, $TOTALTESTRESULTS total test results,  and $HOSPITALIZED hospitalized."

