#!/bin/bash
if [$1 = ""];then
echo "请输入<main-action>参数。"
elif [$2 = ""];then
echo "请输入<additional-action>参数。"
else
python3 main.py $0 $1
fi
