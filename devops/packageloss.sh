#!/bin/bash

TARGETS=("8.8.8.8" "1.1.1.1" "google.com")

while true; do
    echo "===== $(date '+%Y-%m-%d %H:%M:%S') ====="

    for target in "${TARGETS[@]}"; do
        result=$(ping -c 1 -W 2 "$target" 2>&1)

        if echo "$result" | grep -q "1 packets transmitted, 1 received"; then
            latency=$(echo "$result" | grep 'time=' | sed -E 's/.*time=([0-9.]+).*/\1/')
            echo "$target -> OK (${latency} ms)"
        else
            echo "$target -> PACKET LOSS"
        fi
    done

    echo
    sleep 1
done