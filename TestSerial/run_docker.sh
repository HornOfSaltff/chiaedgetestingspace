#!/bin/bash


hash=$(git rev-parse --short HEAD)

echo $hash

DEVICES=""

ports=$(python3 -m serial.tools.list_ports)
echo $ports
if [[ "$ports" == *"no ports found" ]]; then
  devices = ""
  echo "No devices: $devices"
else
    for device in $ports
    do
        echo "--device=$device "
        DEVICES+="--device=$device "
    done
fi
echo  "$DEVICES"

docker run $DEVICES ecy14mhfh/testserial:$hash

#if ports devices = a string of properly formatted devices


#docker run --device=/dev/ttyACM0 --device=/dev/ttyACM1 --device=/dev/ttyUSB0 --device=/dev/ttyUSB1 ecy14mhfh/testserial:$hash