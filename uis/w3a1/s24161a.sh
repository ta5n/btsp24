#!/bin/bash
if [[ $# -ne 8 ]]; then
	echo -e "Kullanim:\n"
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
if [[ ! -f "$baboliDizini/enc.txt" ]]; then
	echo "$baboliDizini/enc.txt dosyasi bulunamadi"
	exit 2
fi
if [[ ! -f "$baboliDizini/baboli.txt" ]]; then
	echo "$baboliDizini/baboli.txt dosyasi bulunamadi"
	exit 2
fi
if [[ ! -d "$aliyeDizini" ]]; then
	echo "$aliyeDizini dizini bulunamadi"
	exit 2
fi

while IFS= read -r LINE || [[ -n "$LINE" ]]; do
    if [[ -z "$LINE" || "$LINE" -lt 1 ]]; then
        echo "enc.txt formati bozuk";
        exit 2
    fi
    arrAliyeLineNumbers[$i]="$LINE"
    (( i++ ))
done < <(head --lines="$satirSayisi" "$baboliDizini/enc.txt")

(( i=1 ))
while IFS= read -r LINE || [[ -n "$LINE" ]]; do
    if [[ -z "$(echo "$LINE" | cut -c 2-)" || $(echo "$LINE" | cut -c 2-) -lt 1 ]]; then
        echo "baboli.txt formati bozuk";
        exit 2
    fi
    count=$(echo "$LINE" | cut -c 2-)
    if [[ -z "$(echo "$LINE" | cut -c 1)" ]]; then
        echo "baboli.txt formati bozuk"
        exit 2
    fi
    ordLetter=$(printf '%d' "'$(echo "$LINE" | cut -c 1)")
    cryptLetter=$(((ordLetter * count + anahtar) % 74 + 48))
    arrAliyeLetters[$i]=$(printf \\$(printf '%03o' $cryptLetter))
    (( i++ ))
done < <(head --lines="$satirSayisi" "$baboliDizini/baboli.txt")

for i in "${arrAliyeLineNumbers[@]}"; do
    echo "${arrAliyeLetters[$i]}" >> "$aliyeDizini/aliye.txt"
done
