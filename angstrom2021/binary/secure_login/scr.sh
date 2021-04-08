#!/bin/bash

for ((i=0;i<1000;i++)); do
    echo -e '\x00' | ./login
done