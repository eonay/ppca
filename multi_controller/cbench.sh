#!/bin/bash
#
# https://github.com/trema/cbench
#
c0="192.168.219.111"
c1="192.168.219.222"

cd ..
cd cbench
 ./bin/cbench -c $c0 --port 6653 --switches 8 --loops 10 --ms-per-test 10000 --delay 1000 --throughput &

./bin/cbench -c $c1 --port 6653 --switches 8 --loops 10 --ms-per-test 10000 --delay 1000 --throughput 




