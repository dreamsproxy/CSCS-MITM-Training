# CSCS Network Security Training Toolkit
# Topic: Network Traffic
***

##This a project for the Civil Society Cyber Shield

The primary goal of this to to develop a project to showcase how network traffic is easily observable under connections using http protocols or witout VPN.

### Specifcations
Vagrant Image Sharing for Quick deploy
VBox OVA Image (OVF Standard)

### Features
Auto wireless interface detection
Use detected W-LAN driver to create a Rouge-WAP
Bridge Rouge-WAP to NAT (Host network)
Start Wireshark on selected W-LAN Adapater
Auto-generated Vagrant environment with tools
Tookit hosted in OVA Image
Quick VBox image import


***
## How it works
#### Step 1
Download the Pre-packaged OVA Image.

#### Step 2
Using Oracle VBox, import the downladed OVA Image.

#### Step 3
Plug in your network driver into your machine's USB port.

#### Step 4
Start the virtual machine (VM)
Wait until the virtual machine has fully booted.
*You will see a login screen*
Login into the virtual machine

#### Step 5
Once you have logged on, connect the WLAN driver to the virtual machine
Wait 5 seconds

#### Step 6
There will be 1 application on the desktop named `Auto-Wireshark`
Double click it

The system should automatically start wireshark on the interface you switched to.
***
### Dev Setup
Run `setup.sh` as root user
Example: `sudo setup.sh`
The above script generates and setups a Ubuntu LTS 20.04 Vbox Image with the toolkit pre-packaged

***
## Possible Future Works
DNS Spoofing (IP Redirect)
ARP Poisoning and Redirect (Data Redirection)
SSL Cert Spoofing
Proxy Spoofing
MAC Spoofing
IP Spoofing
MITM Routing (Ettercap?)