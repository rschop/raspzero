#! /bin/bash
# echo "Hello World"

i=1
while [[ $i -le 100 ]] ; do
	echo "$i"
  	# (( i += 1 ))
	curl -i https://raschop-eval-test.apigee.net/v1/ingestlog/json?apikey=RceQYv4yjAvmljUjaE1RmFARXJ8cSFf0
	sleep $[ ( $RANDOM % 300) ]s
done
