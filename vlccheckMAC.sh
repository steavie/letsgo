#!/bin/sh
PID=$(pgrep VLC)
echo $PID
if $PID <> '0'
 then  /Applications/VLC.app/Contents/MacOS/VLC  http://p.live.fra.n-tv.de/hls-live/ntvlive/ntvlive_1500.m3u8 --volume 500
 fi
