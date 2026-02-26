#!/bin/bash

for moi in {1..10}
do
	echo "--- MOI: $moi ---"
	sed -i "s/\(MOI \)[0-9]*/\1$moi/" "lambda.in"
	./aleae lambda.in lambda.r 1000 -1 0 | grep -E "^avg|^cI2 >= 145:|^Cro2 >= 55:"
	echo ""
done
