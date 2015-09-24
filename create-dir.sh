#!/usr/bin/bash

cd work
for i in *
do
	a=`echo $i | sed -e 's/\(.*\).txt/\1/'`
	mkdir $a
	mv $i $a
done
cd ..
