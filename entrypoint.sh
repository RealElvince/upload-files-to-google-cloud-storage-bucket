#!/bin/bash
set -e

# List contents to debug
echo "Listing directory contents:"
ls -la /app
ls -la /app/scripts

# run generate_data.py
echo "Running generate_data.py..."
python3 /app/scripts/generate_data_script.py
# run create_bucket.py
echo "Running create_bucket.py..."
python3 /app/scripts/create_bucket.py

# run upload_files to gcs bucket
echo "Running upload_files.py..."
python3 /app/scripts/upload_files.py