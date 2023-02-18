#!/bin/bash

# Function to clean up and exit
function cleanup {
  echo "Exiting script..."
  kill 0
}

# Function to print the help message
function usage {
  echo "Usage: $0 [-i input_dir] [-o output_dir] [-p parallelism]"
  echo "Decompiles all .pyc files in the specified input directory and writes the output to the specified output directory using parallelism level specified."
  echo ""
  echo "Options:"
  echo "-i, --input-dir  The input directory to search for .pyc files. Default is 'data/sims4-not-yet-decompiled'."
  echo "-o, --output-dir The output directory to write decompiled .py files. Default is 'data/sims4-decompiled'."
  echo "-p, --parallelism The level of parallelism to use. Default is '1'."
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
    -p|--parallelism)
    parallelism="$2"
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
parallelism=${parallelism:-"1"}

# Create the output directory if it doesn't exist
if [ ! -d "$output_dir" ]; then
  mkdir -p "$output_dir"
fi

# Set up the trap for the SIGINT signal
trap cleanup SIGINT

# Use GNU parallel to execute the loop in parallel
find "$input_dir" -type d | parallel -j "$parallelism" '
  output_subdir="$output_dir/${1#"$input_dir/"}"
  if [ ! -d "$output_subdir" ]; then
    mkdir -p "$output_subdir"
  fi
  for file in "{}"/*.pyc; do
    if [ -f "$file" ]; then
      output_file="$output_subdir/${file##*/}"
      output_file="${output_file%.*}.py"
      if [ -f "$output_file" ] && [ "$output_file" -nt "$file" ]; then
        echo "Skipping file: $file (already decompiled)"
      else
        echo "Decompiling file: $file"
        uncompyle6 "$file" > "$output_file"
      fi
    fi
  done
'

# Exit cleanly
cleanup

