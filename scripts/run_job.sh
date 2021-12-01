#!/usr/bin/env bash

## Complete the following steps to run exchange rate cron job

# Step 1:
# Create virtual environment
python3 -m venv ~/.venv

# Step 2: 
# Source newly created virtual environment
source ~/.venv/bin/activate

# Step 3: 
# Install app dependencies
pip install --upgrade pip && pip install -r requirements.txt

# Step 4: 
# Run application
cd scripts
python3 ./forex.py

