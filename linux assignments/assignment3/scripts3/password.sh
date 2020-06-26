#!/bin/bash

echo -n 'Enter the length of password: '
read n
head /dev/urandom | tr -dc A-Za-z0-9 | head -c $n ; echo ''