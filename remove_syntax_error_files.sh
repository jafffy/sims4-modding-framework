#!/bin/bash

# Function to clean up and exit
function cleanup {
  echo "Exiting script..."
  kill 0
}

# Function to print the help message
function usage {
  echo "Usage: $0 <directory>"
  echo "Removes all grammatically wrong Python files in the specified directory and its subdirectories."
}

# Set up the trap for the SIGINT signal
trap cleanup SIGINT

# Parse command line arguments
if [[ $# -ne 1 ]]; then
  usage
  exit 1
fi

dir=$1

# Remove all grammatically wrong Python files in the directory and its subdirectories
find "$dir" -name "*.py" -type f -print0 | while read -d $'\0' file
do
  if ! python3.7 -m py_compile "$file"; then
    echo "Removing file: $file (syntax error)"
    rm "$file"
  fi
done

echo "Done."

