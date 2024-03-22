#!/bin/bash

# Function to run the script and measure execution time
benchmark() {
    input_file=$1
    algorithm=$2
    input_type=$3
    algorithm_name=${algorithm_mapping_reverse[$algorithm]}
    # List of supported languages and their run commands
    runrust=""
    runjava=""
    runpython="python3 algorithms.py"
    runcpp=""
    runexample="python3 example.py"
    runcurrent=$runpython

    echo "Benchmarking Algorithm $algorithm with input $input_file"
    result=$(/usr/bin/time -f "%e" ${runcurrent} --algorithm $algorithm < $input_file 2>&1 >/dev/null)
    echo "Result $result"
    time=$(echo $result | head -1)  # Extract real time from the time command output
    echo $time
    size=$(head -n 1 $input_file)
    # Append results to CSV file
    #!/bin/bash

    if [ "$input_type" = "random_array" ]; then
        echo "$algorithm_name,$size,$time" >> benchmark_results_random.csv
    elif [ "$input_type" = "increasing_array" ]; then
        echo "$algorithm_name,$size,$time" >> benchmark_results_increasing.csv
    elif [ "$input_type" = "decreasing_array" ]; then
        echo "$algorithm_name,$size,$time" >> benchmark_results_decreasing.csv
    elif [ "$input_type" = "constant_array" ]; then
        echo "$algorithm_name,$size,$time" >> benchmark_results_constant.csv
    elif [ "$input_type" = "a_shaped_array" ]; then
        echo "$algorithm_name,$size,$time" >> benchmark_results_ashaped.csv
    fi
    echo "------------------------"

}

# Map algorithm names to numbers
declare -A algorithm_mapping=(
    ["insertion_sort"]=1
    ["shell_sort"]=2
    ["selection_sort"]=3
    ["heap_sort"]=4
    ["quick_sort_left_pivot"]=5
    ["quick_sort_random_pivot"]=6
)

# Create a reverse mapping from numbers to algorithm names
declare -A algorithm_mapping_reverse
for algorithm_name in "${!algorithm_mapping[@]}"; do
    algorithm_number=${algorithm_mapping[$algorithm_name]}
    algorithm_mapping_reverse[$algorithm_number]=$algorithm_name
done



input_files=("random_array" "increasing_array" "decreasing_array" "constant_array" "a_shaped_array")

# Create or clear the CSV file
echo "Algorithm,InputSize,Time" > benchmark_results.csv

# Run the benchmark for each input file, sorting algorithm, and size
for input_type in "${input_files[@]}"; do
    for algorithm_name in "${!algorithm_mapping[@]}"; do
        algorithm_number=${algorithm_mapping[$algorithm_name]}
        for input_file in "benchmark/${input_type}_"*".txt"; do
            benchmark $input_file $algorithm_number $input_type
        done
    done
done