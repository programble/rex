#!/bin/bash
if [ -f ./rex.py ]; then
    python rex.py $@
else
    python /usr/share/rex/rex.py
fi
