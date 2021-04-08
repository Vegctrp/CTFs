#!/bin/bash

for ((i=1;i<=100;i++)); do
    echo $i
    echo %$i\$p | ./stickystacks
done