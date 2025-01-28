#!/usr/bin/bash

if ! pgrep -f 'bot.py'
then
    cd /bots/bot_4_Q || exit; python3 bot.py
else
    echo "running"
fi