#!/usr/bin/bash
# This goes hand in hand with the bifrost tool
# it takes a payload and reads each line to stdout
# stdout is redirected to stdin.
# this could also be refined. 
# As is, it does not stop until EOF
# Why didn't I do this in python???
# Well, I wanted to write something quickly w/o worrying about subroutines.

payload=payload.txt
max=$(wc -l < $payload)
i=1
while [ $i -le 10000 ]
do
	pl=$(sed "${i}q;d" $payload)
	echo $pl > plt.txt && cat plt.txt
	./nclroot 5dd16a2c0c0daac9cbed76aeb8a00634 < plt.txt >> answer.txt
	unset pl
	i=$(($i+1))
	#sleep 1 
done
