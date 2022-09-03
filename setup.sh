#!/bin/bash
cd
sudo apt install hostapd iproute2 iw util-linux procps wireshark make
git clone https://github.com/oblique/create_ap
cd create_ap
make install
cd ..
sudo rm -rf create_ap
