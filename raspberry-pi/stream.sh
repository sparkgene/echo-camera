#!/bin/bash

base="/var/www/html"

cd $base
rm -f stream.m3u8
rm -f segments/*.ts

raspivid -n -w 720 -h 405 -fps 25 -vf -t 86400000 -b 1800000 -ih -o - \
| ffmpeg -y \
    -i - \
    -c:v copy \
    -map 0:0 \
    -f ssegment \
    -segment_time 2 \
    -segment_format mpegts \
    -segment_list "$base/stream.m3u8" \
    -segment_list_size 5 \
    -segment_list_flags live \
    -segment_list_type m3u8 \
    -segment_list_entry_prefix segments/ \
    "$base/segments/%08d.ts"