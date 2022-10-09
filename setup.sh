#!/bin/sh

echo -e "\e[1;42m[ARIVA] Starting setup"

python3.9 -m pip install -r requirements.txt
git fetch

echo -e "\e[1;42m[ARIVA] Setup complete"

echo -e "\e[1;42m[ARIVA] Starting server\e[1;37m"
python3.9 flask/app.py
