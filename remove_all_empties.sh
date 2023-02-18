#!/bin/bash

# Function to print the help message
function usage {
  echo "Usage: $0 <directory>"
  echo "Removes all empty files in the specified directory and its subdirectories."
}

# Parse command line arguments
if [[ $# -ne 1 ]]; then
  usage
  exit 1
fi

dir=$1

# Remove all empty files in the directory and its subdirectories
find "$dir" -type f -empty -delete

echo "Done."

