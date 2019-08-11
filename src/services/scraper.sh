#!/bin/sh
timeout -s SIGINT $2 ffmpeg -nostdin -i $(youtube-dl -f $4 -g $1) $3
