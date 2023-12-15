#!/bin/sh
javac $1.java
sleep 0.1
cat input.txt | java $1