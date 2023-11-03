#!/usr/bin/env bash
export TZ=Asia/Tokyo
out1=htmlout
out2=xmlout
[ -d "$out1" ] || mkdir -p $out1
[ -d "$out2" ] || mkdir -p $out2
for((i=7;i>0;--i))
{
    D=$(date --date "$i days ago" '+%Y%m%d')
    # echo $D
    for j in $(seq -w 0 23); do
        # wget -c "https://tenhou.net/sc/raw/dat/scc$D$j.html.gz" -O "$out1/$D$j.html.gz"
        # gzip -d "$out1/$D$j.html.gz"
        python3 getxml.py "$out1/$D$j.html" | while read -r line; do
            wget -c "http://tenhou.net/0/log/?$line" -O "$out2/$line.xml"
        done
    done
}
