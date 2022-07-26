#!/bin/bash
sudo apt install hostapd iproute2 iwconfig util-linux procps
git clone https://github.com/oblique/create_ap
cd create_ap
make install
cd ..
sudo rm -rf create_ap