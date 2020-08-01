#!/bin/bash

COUNT=$(echo `ls ../memedisk/memes | wc -l` )
WEIGHT=$(echo `du -sh ../memedisk/memes | awk {'print $1'}`)

echo COUNT OF MEMES: $COUNT
echo TOTAL WEIGHT OF MEMES: $WEIGHT
