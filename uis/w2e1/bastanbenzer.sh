#!/bin/bash
if [[ $# -ne 3 ]]; then
	echo -e "Usage:\n   bastangoster n file1 file2\n\n"
	echo -e "   n is number of lines from top to compare\n"
	echo -e "   file1 and file2 the files to be compared\n"
	exit 2
fi

n=$1
file1=$2
file2=$3

if [[ ! -f $file1 ]]; then
	echo "$file1 does not exist"
	exit 2
fi
if [[ ! -f $file2 ]]; then
	echo "$file2 does not exist"
	exit 2
fi


f1linecount=$(wc -l <"$file1")
f2linecount=$(wc -l <"$file2")

if [[ $f1linecount -lt $n || $f2linecount -lt $n ]]; then
	echo "farkli"
	exit 1
fi

if [[ $(diff  <(head --lines="$n" "$file1") <(head --lines="$n" "$file2") > /dev/null) -eq 0 ]]; then
	echo "ayni"
	exit 0
else
	echo "farkli"
	exit 1
fi
