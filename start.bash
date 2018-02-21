#!/usr/bin/env bash

# generating random mac-address
# openssl rand -hex 6 | sed ‘s/\(..\)/\1:/g; s/.$//’

# view mac address
# ifconfig en0

# specifiy new mac address
# sudo ifconfig en0 ether xx:xx:xx:xx:xx:xx

# prompt user to change mac address
echo "Change your mac-address"

# restarting en0
# sudo ifconfig en0 down
# sudo ifconfig en0 ether xx:xx:xx:xx:xx:xx
# sudo ifconfig en0 up


