#!/bin/bash

# Exit script on error
set -e

# Run the schema creation script
echo "Creating Weaviate schema..."
python create_schema.py

# Assuming create_schema.py exits without error, proceed to index data
echo "Indexing data into Weaviate..."
python index_data.py

echo "Backing up data into from Weaviate to MinIO..."
python backup_s3.py

# Keep the container running after scripts execution
# This line is useful if you want to prevent the container from exiting after the scripts complete.
# If your container should close after execution, you can comment or remove this line.
tail -f /dev/null