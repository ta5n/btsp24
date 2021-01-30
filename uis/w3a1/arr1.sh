#!/bin/bash
if [[ $# -ne 8 ]]; then
	echo -e "Usage:\n"
    echo -e "./s24161.sh -b <babolidizini> -a <aliyedizini> -n <satirsayisi> -m <anahtar>\n"
	exit 2
fi
if [[ $1 -eq "-b" ]]; then
    baboliDizini=$2
fi
if [[ $3 -eq "-a" ]]; then
    aliyeDizini=$4
fi
if [[ $5 -eq "-n" ]]; then
    satirSayisi=$6
fi
if [[ $7 -eq "-m" && $8 -le 99 ]]; then
    anahtar=$8
else
    echo "Anahtar 1-99 arasinda olmalidir"
    exit 2
fi
if [[ ! -d "$baboliDizini" ]]; then
	echo "$baboliDizini dizini bulunamadi"
	exit 2
fi
if [[ ! -d "$aliyeDizini" ]]; then
	echo "$aliyeDizini dizini bulunamadi"
	exit 2
fi

readarray -t arrEnc < ./giden/enc.txt

echo ${arrEnc[@]}

readarray -t arrBaboli < ./giden/baboli.txt

for b in $arrBaboli; do
  letter=$(echo $b | cut -c 1)
  count=$(echo $b | cut -c 2-)
  ordLetter=$(printf '%d' "'$letter")
  cryptLetter=$((($ordLetter * $count + $anahtar) % 74 + 48))
  arrAliyeLetters+=$(printf \\$(printf '%03o' $cryptLetter))
done
echo ${arrAliyeLetters[@]}
echo 

for i in "${arrEnc[@]}"; do
    echo "${arrAliyeLetters[$i]}" >> $aliyeDizini/aliye.txt
done
