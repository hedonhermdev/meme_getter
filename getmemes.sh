#!/usr/bin/env bash

/Users/tirthjain/anaconda/bin/python3 --version
echo -e "GET http://google.com HTTP/1.0\n\n" | nc google.com 80 > /dev/null 2>&1

if [ $? -eq 0 ]; then
    /Users/tirthjain/anaconda/bin/python3 memes2.py $1 $2
    echo "Successfully got memes, sucker."
else
    echo "No internet connection, biyatch."

fi
