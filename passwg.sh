#!/bin/bash
cat /dev/urandom | tr -dc 'A-Za-z0-9' | fold -w 10 | head -n 1

