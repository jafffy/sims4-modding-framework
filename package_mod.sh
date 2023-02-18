#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <relative path to Python source file>"
    exit 1
fi

# Get the relative path of the file from the command-line parameter
FILE_PATH=$1

# Extract the filename without extension from the path
TARGET_MOD=$(basename "${FILE_PATH}" .py)

# Compile the Python source code
python3.7 -m py_compile "${FILE_PATH}"

# Make a directory for the target module
mkdir "${TARGET_MOD}"

# Copy the source code and compiled output to the target directory
cp "${FILE_PATH}" "./${TARGET_MOD}/${TARGET_MOD}.py"
cp "$(dirname ${FILE_PATH})/__pycache__/${TARGET_MOD}.cpython-37.pyc" "./${TARGET_MOD}/${TARGET_MOD}.pyc"

# Zip up the source code and compiled output
zip "${TARGET_MOD}.zip" "./${TARGET_MOD}/${TARGET_MOD}.py" "./${TARGET_MOD}/${TARGET_MOD}.pyc"

