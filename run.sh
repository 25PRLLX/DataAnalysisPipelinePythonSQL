#!/bin/bash

set -e

set -x

python setup_database.py

python -m database

python data_analysis.py

python data_visualization.py

echo "All scripts executed successfully."