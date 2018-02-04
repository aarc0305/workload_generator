#!/bin/bash

INTERVAL="1"

function monitor() {
    RPKT1=`cat /sys/class/net/$TAP/statistics/rx_bytes`
    TPKT1=`cat /sys/class/net/$TAP/statistics/tx_bytes`
    sleep $INTERVAL
    RPKT2=`cat /sys/class/net/$TAP/statistics/rx_bytes`
    TPKT2=`cat /sys/class/net/$TAP/statistics/tx_bytes`
    RXDiff=`expr $RPKT2 - $RPKT1`
    TXDiff=`expr $TPKT2 - $TPKT1`
    echo "$1 TX: $TXDiff bytes/sec RX: $RXDiff bytes/sec"
}

if [[ $# -ne 1 ]]; then
    echo "Illegal number of parameters."
    echo "sudo ./pkt_monitor.sh <monitored_tap>"
    exit 1
fi

test -e /sys/class/net/$1/statistics/rx_bytes
if [ $? -ne 0 ]; then
    echo "$1 does not exist."
    exit 1
else
    TAP=$1
fi

while true
do
    monitor
done
