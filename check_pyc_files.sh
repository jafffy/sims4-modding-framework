#!/bin/bash

# Print help message if script is called with no parameters or the wrong number of parameters
if [ $# -ne 2 ] || [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
    echo "Usage: $0 dirA dirB"
    echo "  dirA: path to directory A containing *.pyc files"
    echo "  dirB: path to directory B containing corresponding *.py files"
    exit 1
fi

# Set the directory paths for A and B
dirA="$1"
dirB="$2"

# Check that the directory paths are valid
if [ ! -d "$dirA" ]; then
    echo "Error: $dirA is not a directory"
    exit 1
fi

if [ ! -d "$dirB" ]; then
    echo "Error: $dirB is not a directory"
    exit 1
fi

# Loop through the *.pyc files in directory A and its subdirectories
find "$dirA" -name "*.pyc" -print0 | while read -d $'\0' file; do
    # Extract the base filename without the extension
    base=$(basename "$file" .pyc)
    # Get the subdirectory path relative to directory A
    sub_dir=$(dirname "$file" | sed "s|$dirA/||")
    # Check if the corresponding *.py file exists in directory B
    if [ ! -e "$dirB/$sub_dir/$base.py" ]; then
        echo "./$sub_dir/$base.pyc failed to generate ./$sub_dir/$base.py in directory B"
    fi
done

