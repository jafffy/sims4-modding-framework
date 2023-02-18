#!/bin/bash

# Function to clean up and exit
function cleanup {
  echo "Exiting script..."
  kill 0
}

# Function to print the help message
function usage {
  echo "Usage: $0 [-i input_dir] [-o output_dir]"
  echo "Decompiles all .pyc files in the specified input directory and writes the output to the specified output directory."
  echo ""
  echo "Options:"
  echo "-i, --input-dir  The input directory to search for .pyc files. Default is 'data/sims4-not-yet-decompiled'."
  echo "-o, --output-dir The output directory to write decompiled .py files. Default is 'data/sims4-decompiled'."
  echo "-h, --help       Show this help message and exit."
}

# Parse command line arguments
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -i|--input-dir)
    input_dir="$2"
    shift # past argument
    shift # past value
    ;;
    -o|--output-dir)
    output_dir="$2"
    shift # past argument
    shift # past value
    ;;
    -h|--help)
    usage
    exit 0
    ;;
    *)
    # unknown option
    echo "Unknown option: $1"
    usage
    exit 1
    ;;
esac
done

# Set default values if parameters are not set
input_dir=${input_dir:-"data/sims4-not-yet-decompiled"}
output_dir=${output_dir:-"data/sims4-decompiled"}

# Create the output directory if it doesn't exist
if [ ! -d "$output_dir" ]; then
  mkdir -p "$output_dir"
fi

# Set up the trap for the SIGINT signal
trap cleanup SIGINT

# Loop through all subdirectories recursively
for dir in $(find "$input_dir" -type d); do
  # Get the path of the corresponding subdirectory in the output directory
  relative_path=${dir#"$input_dir/"}
  output_subdir="$output_dir/$relative_path"

  # Create the corresponding subdirectory in the output directory if it doesn't exist
  if [ ! -d "$output_subdir" ]; then
    mkdir -p "$output_subdir"
  fi

  # Loop through all '.pyc' files in the subdirectory
  for file in "$dir"/*.pyc; do
    # Check if the file exists and is a regular file
    if [ -f "$file" ]; then
      # Get the path of the output file
      output_file="$output_subdir/${file##*/}"
      output_file="${output_file%.*}.py"

      # Check if the output file already exists and is newer than the input file
      if [ -f "$output_file" ] && [ "$output_file" -nt "$file" ]; then
        # If the output file exists and is newer, skip decompilation and print a message
        echo "Skipping file: $file (already decompiled)"
      else
        # Otherwise, print the name of the file being decompiled and decompile it
        echo "Decompiling file: $file"
        uncompyle6 "$file" > "$output_file"
      fi
    fi
  done
done

# Exit cleanly
cleanup

