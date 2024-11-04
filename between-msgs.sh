# between-msgs.sh
#!/bin/bash
awk -v min="$2" -v max="$3" '$3 >= min && $3 <= max' "$1"

