#!/usr/bin/bash

if ! pgrep -f 'bot.py'
then
    cd /var/www/fastuser/data/bot || exit; python3 bot.py
else
    echo "running"
fi