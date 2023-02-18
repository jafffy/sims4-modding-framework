#!/bin/bash

# Function to clean up and exit
function cleanup {
  echo "Exiting script..."
  kill 0
}

# Set the input and output directories
input_dir="data/sims4-not-yet-decompiled"
output_dir="data/sims4-decompiled"

# Create the output directory if it doesn't exist
if [ ! -d "$output_dir" ]; then
  mkdir -p "$output_dir"
fi

# Set up the trap for the SIGINT signal
trap cleanup SIGINT

# Define a function to check a single pyc file
function check_pyc_file {
  file="$1"
  relative_path=$(dirname "$file" | sed "s|$input_dir/||")
  output_subdir="$output_dir/$relative_path"
  base=$(basename "$file" .pyc)
  output_file="$output_subdir/$base.py"
  if [ ! -e "$output_file" ]; then
    echo "./$relative_path/$base.pyc failed to generate ./$relative_path/$base.py in directory $output_dir"
  fi
}

# Export the check_pyc_file function to make it available to xargs
export -f check_pyc_file

# Find all the *.pyc files and pass them to xargs to run the check in parallel
find "$input_dir" -name "*.pyc" -print0 | xargs -0 -I{} -P "$(nproc)" bash -c 'check_pyc_file "$@"' _ "{}"

# Exit cleanly
cleanup

