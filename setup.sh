#!/bin/bash

echo -e "\e[1;42m[ARIVAAA] Starting setup"

python3.9 -m pip install -r requirements.txt
git fetch

echo -e "\e[1;42m[ARIVAAA] Setup complete"

echo -e "\e[1;42m[ARIVAAA] Starting server"
python3.9 flask/app.py