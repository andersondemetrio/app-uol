# order-by-username.sh
#!/bin/bash
if [ "$2" == "-desc" ]; then
    sort -k1,1r "$1"
else
    sort -k1,1 "$1"
fi

