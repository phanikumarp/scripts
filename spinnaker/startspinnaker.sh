#!/bin/bash
cd /home/ubuntu/build

../spinnaker/dev/run_dev.sh clouddriver
sleep 5
../spinnaker/dev/run_dev.sh rosco
sleep 2
../spinnaker/dev/run_dev.sh igor
sleep 2
../spinnaker/dev/run_dev.sh orca
sleep 2
../spinnaker/dev/run_dev.sh echo
sleep 2
../spinnaker/dev/run_dev.sh gate
sleep 5
cd front50
nohup ./gradlew bootRun &
cd ..
../spinnaker/dev/run_dev.sh deck
sleep 5
#cd ../deck
#API_HOST=http://localhost:8084 yarn run start
