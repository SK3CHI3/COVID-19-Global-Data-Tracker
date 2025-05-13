#!/bin/bash

# COVID-19 Global Data Tracker - Run Script

echo "Setting up COVID-19 Global Data Tracker..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3 and try again."
    exit 1
fi

# Check if the data file exists
if [ ! -f "data/owid-covid-data.csv" ]; then
    echo "Downloading COVID-19 dataset..."
    mkdir -p data
    curl -L -o data/owid-covid-data.csv https://covid.ourworldindata.org/data/owid-covid-data.csv
fi

# Note about dependencies
echo "Note: This script assumes you have the required Python packages installed."
echo "If you encounter errors, please install the packages listed in requirements.txt manually."
echo ""

# Check if Jupyter is available
if command -v jupyter &> /dev/null; then
    echo "Launching Jupyter Notebook..."
    cd notebooks
    jupyter notebook COVID19_Global_Data_Analysis.ipynb
else
    echo "Jupyter is not installed. You can view the notebook file directly:"
    echo "notebooks/COVID19_Global_Data_Analysis.ipynb"

    # Alternative: Display the notebook content
    echo ""
    echo "Displaying notebook content (Python code only):"
    echo "----------------------------------------"
    grep -A 5 "cell_type\": \"code" notebooks/COVID19_Global_Data_Analysis.ipynb | grep "source" | sed 's/^.*source\": \[//' | sed 's/\],$//' | sed 's/\\n/\n/g' | sed 's/^"//' | sed 's/"$//'
fi
