# max-min-size.sh
#!/bin/bash
if [ "$2" == "-min" ]; then
    sort -k4,4 -n "$1" | head -n 1
else
    sort -k4,4 -nr "$1" | head -n 1
fi

