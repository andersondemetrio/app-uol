#!/bin/bash


convert_to_int() {
    echo "$1" | sed 's/^0*//' | tr -d ' '
}

convert_to_size() {
    echo "$1" | sed 's/^0*//' | tr -d ' '
}


if [ $# -eq 0 ]; then
    echo '{"error": "No input file provided"}'
    exit 1
fi

input_file="$1"


while IFS= read -r line || [[ -n "$line" ]]; do
   
    email=$(echo "$line" | awk '{print $1}')

    
    number_messages=$(echo "$line" | awk '{for(i=2;i<=NF;i++) if($i~/^size/) print $i}' | head -n 1 | convert_to_int)

    
    size=$(echo "$line" | awk '{for(i=2;i<=NF;i++) if($i~/^size/) print $i}' | tail -n 1 | convert_to_size)

   
    echo "{\"username\":\"$email\",\"folder\":\"$(echo "$line" | awk '{for(i=2;i<=NF;i++) if($i~/^folder/) print $i}')\",\"numberMessages\":$number_messages,\"size\":$size}"
done < "$input_file"


if [ $? -eq 1 ]; then
    echo '{"error": "No input file provided"}'
fi

